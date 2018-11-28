#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, m;
	cin >> n >> m;
	vector <string> a(n);
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			//cerr << i << ' ' << j << endl;
			if (a[i][j] == '.') {
				continue;
			}
			int c = 0;
			for (int k = 0; k < n; ++k) {
				if (a[k][j] != '.') {
					c++;
				}
			}
			for (int k = 0; k < m; ++k) {
				if (a[i][k] != '.') {
					c++;
				}
			}
			if (c - 2) {
				continue;
			} else {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}
	}
	int ans = 0;
	vector <vector <bool> > ch(n, vector <bool> (m, 0));
	for (int i = 0; i < n; ++i) {
		int f = m, l = -1;
		for (int j = 0; j < m; ++j) {
			if (a[i][j] != '.') {
				f = min(f, j);
				l = max(l, j);
			}
		}
		//cerr << f << ' ' << l << endl;
		if (l == -1) {
			continue;
		}
		if (a[i][f] == '<') {
			ch[i][f] = 1;
		}
		if (a[i][l] == '>') {
			ch[i][l] = 1;
		}
	}
	for (int j = 0; j < m; ++j) {
		int f = n, l = -1;
		for (int i = 0; i < n; ++i) {
			if (a[i][j] != '.') {
				f = min(f, i);
				l = max(l, i);
			}
		}
		if (l == -1) {
			continue;
		}
		if (a[f][j] == '^') {
			ch[f][j] = 1;
		}
		if (a[l][j] == 'v') {
			ch[l][j] = 1;
		}
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			ans += ch[i][j];
		}
	}
	cout << ans << endl;
	return;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
		solve();
	}
}