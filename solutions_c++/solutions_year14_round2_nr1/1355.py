#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;

char words[100][101];
char s1[101], s2[101];
int lengths[100][100];
int l1, l2;

ifstream fin("input.in");
ofstream fout("output.out");

int ispossible(int i, int j) {
	int modif, possible;
	strcpy(s1, words[i]);
	strcpy(s2, words[j]);

	l1 = strlen(s1);
	l2 = strlen(s2);
	possible = 1;
	modif = 0;
	for(i = 0, j = 0; i < l1 && j < l2 && possible == 1;) {
		if(s1[i] == s2[j]) {
			i++;
			j++;
		} else {
			if(s1[i-1] == s2[j]) {
				j++;
				modif++;
			} else {
				if(s1[i] == s2[j-1]) {
					i++;
					modif++;
				} else {
					possible = 0;
				}
			}
		}
	}
	if(possible == 1 && i < l1) {
		// for finished because j = l2-1
		for(; i < l1; i++) {
			if(s1[i] == s2[l2-1]) {
				modif++;
			} else {
				possible = 0;
			}
		}
	}
	if(possible == 1 && j < l2) {
		for(; j < l2; j++) {
			if(s2[j] == s1[l1-1]) {
				modif++;
			} else {
				possible = 0;
			}
		}
	}
	if(possible == 0) return -1;
	return modif;
}

int magic(int p, int n) {
	int maxim = 0, i, j, sum, ans = 100000000;
	for(i = 0; i < n; i++) {
		if(lengths[i][p] > maxim) maxim = lengths[i][p];
	}
	for(i = 1; i <= maxim; i++) {
		sum = 0;
		for(j = 0; j < n; j++) {
			sum += abs(lengths[j][p] - i);
		}
		if(sum < ans) ans = sum;
	}
	return ans;
}

int main() {
	int t, it, i, modif, l, n, ans, count, j, part;
	fin >> t;
	for(it = 1; it <= t; it++) {
		fin >> n;
		ans = 0;
		for(i = 0; i < n; i++) {
			fin >> words[i];
		}

		for(i = 1; i < n; i++) {
			modif = ispossible(i, 0);
			if(modif == -1) break;
		}

		if(modif == -1) {
			fout << "Case #" << it << ": Fegla Won\n";
			continue;
		}

		for(i = 0; i < n; i++) {
			count = 1;
			l = strlen(words[i]);
			part = 0;
			for(j = 1; j < l; j++) {
				if(words[i][j] != words[i][j-1]) {
					lengths[i][part++] = count;
					count = 1;
				} else count++;
			}
			lengths[i][part++] = count;
		}

		for(i = 0; i < part; i++) {
			ans += magic(i, n);
		}
		fout << "Case #" << it << ": " << ans << "\n";
	}
	return 0;
}
