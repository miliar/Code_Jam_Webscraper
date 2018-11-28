#include<fstream>
#include<vector>
#include<cstring>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

char cars[10][150];
vector<int> adj[10];
int viz[10], stack[10], total, letters[26], ans, current;
bool ok;
int n;

void verify() {
//	fout << "TANA" << endl;
	int i, j, len;
	for(i = 0; i < n; i++) {
		current = stack[i];
	//	fout << cars[current] << endl;
		len = strlen(cars[current]);
		if(i == 0) letters[cars[current][0] - 'a']++;
		else {
			if(cars[current][0] != cars[stack[i-1]][strlen(cars[stack[i-1]]) - 1]) {
			/*	fout << endl << cars[current][0] << " " << cars[stack[i-1]][strlen(cars[stack[i-1]]) - 1] << endl;
				fout << "* " << cars[stack[i-1]] << endl;*/
				letters[cars[current][0] - 'a']++;
			}
		}
		for(j = 1; j < len; j++) {
			if(cars[current][j] != cars[current][j-1]) {
				letters[cars[current][j] - 'a']++;
			}
		}
	}
	bool ok = true;
	for(i = 0; i < 26; i++) {
	//	fout << i << " - " << letters[i] << endl;
		if(letters[i] > 1) ok = false;
		letters[i] = 0;
	}
	if(ok == true) {
		ans++;
		if(ans >= 1000000007) {
			ans -= 1000000007;
		}
	}
}

void dfs() {
	if(total == n) {
		verify();
	} else {
		int i;
		for(i = 0; i < n; i++) {
			if(viz[i] == 0) {
				viz[i] = 1;
				stack[total++] = i;
				dfs();
				total--;
				viz[i] = 0;
			}
		}
	}
}

void init() {
	int i;
	for(i = 0; i < 26; i++) letters[i] = 0;
	for(i = 0; i < n; i++) {
		viz[i] = 0;
		adj[i].clear();
		ans = 0;
	}
}

int main() {
	int t, i, it, j;
	fin >> t;
	for(it = 1; it <= t; it++) {
		fin >> n;
		init();
		for(i = 0; i < n; i++) {
			fin >> cars[i];
		}
		for(i = 0; i < n; i++) {
			for(j = i + 1; j < n; j++) {
				adj[i].push_back(j);
				adj[j].push_back(i);
			}
		}
	//	stack[0] = 0;
	//	stack[1] = 1;
	//	stack[2] = 2;
	//	verify();
		dfs();
		fout << "Case #" << it << ": " << ans << "\n";
	}
	return 0;
}
