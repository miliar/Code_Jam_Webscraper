#include <iostream>
#include <vector>
#include <string>
#include <memory.h>
#include <set>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <queue>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int maxn = 110;

int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	
	int t;
	cin >> t;

	for (int idx = 1; idx <= t; idx++) {
		int r, c;
		char m[maxn][maxn] = { 0 };
		int d[maxn][maxn] = { 0 };
		int row[maxn] = { 0 };
		int col[maxn] = { 0 };

		cin >> r >> c;
		for (int i = 0; i < r; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < c; j++) {
				m[i][j] = s[j];
				if (m[i][j] != '.') {
					row[i]++;
					col[j]++;
				}
			}
		}

		int marks = 0;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (m[i][j] == '>') {
					int p = j + 1;
					while (p < c && m[i][p] == '.') p++;
					if (p == c) {
						d[i][j] = 1; 
						marks++;
					}
				}

				if (m[i][j] == '<') {
					int p = j - 1;
					while (p >= 0 && m[i][p] == '.') p--;
					if (p == -1) {
						d[i][j] = 1;
						marks++;
					}
				}

				if (m[i][j] == '^') {
					int p = i - 1;
					while (p >= 0 && m[p][j] == '.') p--;
					if (p == -1) {
						d[i][j] = 1;
						marks++;
					}
				}
				
				if (m[i][j] == 'v') {
					int p = i + 1;
					while (p < r && m[p][j] == '.') p++;
					if (p == r) {
						d[i][j] = 1;
						marks++;
					}
				}
			}
		}

		if (marks == 0) {
			cout << "Case #" << idx << ": 0" << endl; 
			continue;
		}

		int ans = 0;
		bool fail = false;
		for (int i = 0; !fail && (i < r); i++) {
			for (int j = 0; !fail && (j < c); j++) {
				if (d[i][j] == 1) {
					if (row[i] == 1 && col[j] == 1) {
						cout << "Case #" << idx << ": IMPOSSIBLE" << endl; 
						fail = true;
					} else {
						ans++;
					}
				}
			}
		}

		if (fail) continue;

		cout << "Case #" << idx << ": " << ans << endl; 
	}

	return 0;
}


