#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

inline bool isVowel(char x) {
	return x == 'a' || x == 'o' || x == 'e' || x == 'u' || x == 'i';
}

void solveTestCase_stupid(string s, int n) {
	long long res = 0;
	for (int i = 0; i < s.size(); ++i) {
		for (int j = i + n - 1; j <= s.size(); ++j) {
			int z = 0;
			for (int k = i; k < j; ++k) {
				if (!isVowel(s[k])) {
					++z;
				} else {
					z = 0;
				}
				if (z == n) {
					++res;
					break;
				}
			}
		}
	}
	cout << res;
}

void solveTestCase() {
	string s;
	int n;
	long long res = 0;
	cin >> s >> n;
	vector<long long> next(s.size());
	int z = 0;
	int last = s.size();
	for (int i = 0; i < s.size(); ++i) {
		if (!isVowel(s[i])) {
			++z;
		} else {
			z = 0;
		}
		if (z >= n) {
			next[i] = 1;
		} else {
			next[i] = 0;
		}
	}
	for (long long i = s.size() - 1; i >= 0; --i) {
		if (next[i]) {
			next[i] = last;
			last = i;
		} else {
			next[i] = -1;
		}
	}
	for (int i = 0; i < next.size(); ++i) {
		if (next[i] != -1) {
			res += (i - n + 2) * (next[i] - i);
		}
	}
	cout << res;
	//solveTestCase_stupid(s, n);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solveTestCase();
		cout << endl;
	}
	return 0;
}