#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#pragma warning (disable : 4996)

// ^ - 1
// > - 2
// v - 3
// < - 4

int main() {
#ifdef _DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T, TT = 0;
	cin >> T;
	while (T-- && ++TT) {
		cout << "Case #" << TT << ": ";
		int n, m;
		cin >> n >> m;
		vector<vector<vector<int>>> v(n);
		vector<vector<int>> p(n, vector<int>(m));
		for (int i = 0; i < n; i++) {
			v[i].resize(m);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				char c;
				cin >> c;
				switch (c) {
				case '^':
					p[i][j] = 1;
					break;
				case '>':
					p[i][j] = 2;
					break;
				case 'v':
					p[i][j] = 3;
					break;
				case '<':
					p[i][j] = 4;
					break;
				}
			}
		}
		// look through rows
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (p[i][j]) {
					v[i][j].push_back(4);
					break;
				}
			}
			for (int j = m - 1; j >= 0; j--) {
				if (p[i][j]) {
					v[i][j].push_back(2);
					break;
				}
			}
		}
		// look through collumns
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n; i++) {
				if (p[i][j]) {
					v[i][j].push_back(1);
					break;
				}
			}
			for (int i = n - 1; i >= 0; i--) {
				if (p[i][j]) {
					v[i][j].push_back(3);
					break;
				}
			}
		}
		bool good = true;
		int ans = 0;
		for (int i = 0; i < n && good; i++) {
			for (int j = 0; j < m && good; j++) {
				if (v[i][j].size() == 4) {
					good = false;
					break;
				}
				bool f = false;
				for (int k = 0; k < v[i][j].size(); k++) {
					if (v[i][j][k] == p[i][j]) {
						f = true;
						break;
					}
				}
				if (f)
					ans++;
			}
		}
		if (good) {
			cout << ans;
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
