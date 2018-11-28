#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

const int C = 27;
const int N = 8;

pair<string, int> z[N] = { make_pair("ONE", 1), make_pair("FIVE", 5), make_pair("SEVEN", 7), make_pair("NINE", 9), make_pair("TEN", 10) };
set<pair<string, int>> zz[C];

bool fill(int l, int c[], vector<int> &res) {
	for (int i = l; i < C; i++) {
		if (c[i] > 0) {
			bool good = true;
			for (set<pair<string, int>>::iterator it = zz[i].begin(); it != zz[i].end(); it++) {
				for (int k = 0; k < it->first.length(); k++) {
					int ci = it->first[k] - 'A';
					c[ci]--;
					good = good && (c[ci] >= 0);
				}
				if (good) {
					res.push_back(it->second);
					if (fill(i, c, res)) {
						return true;
					}
					res.pop_back();
				}
				for (int k = 0; k < it->first.length(); k++) {
					int ci = it->first[k] - 'A';
					c[ci]--;
					good = good && (c[ci] >= 0);
				}
			}
		}
	}
	return true;
}

void rem(int c[], char a, string s, int n, vector<int> &res) {
	while (c[a - 'A'] > 0) {
		for (int i = 0; i < s.length(); i++) {
			c[s[i] - 'A']--;
		}
		res.push_back(n);
		
	}
}

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < z[i].first.length(); j++) {
			zz[z[i].first[j] - 'A'].insert(z[i]);
		}
	}
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int c[C];
		memset(c, 0, C*sizeof(int));
		for (int i = 0; i < s.length(); i++) {
			c[s[i] - 'A']++;
		}

		vector<int> res;

		string s0 = "ZERO";
		string s2 = "TWO";
		string s6 = "SIX";
		string s8 = "EIGHT";
		string s3 = "THREE";
		string s4 = "FOUR";
		string s5 = "FIVE";
		rem(c, 'Z', s0, 0, res);
		rem(c, 'W', s2, 2, res);
		rem(c, 'X', s6, 6, res);
		rem(c, 'G', s8, 8, res);
		rem(c, 'H', s3, 3, res);
		rem(c, 'U', s4, 4, res);
		rem(c, 'F', s5, 5, res);
		rem(c, 'V', "SEVEN", 7, res);
		rem(c, 'O', "ONE", 1, res);
		rem(c, 'N', "NINE", 9, res);

		sort(res.begin(), res.end());
		cout << "Case #" << t << ": ";
		for (int i = 0; i < res.size(); i++) {
			cout << res[i];
		}
		cout << endl;
	}
	return 0;
}