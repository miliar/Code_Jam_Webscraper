#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void solve(int t) {
	int n, m;
	cin >> n >> m;
	vector< vector<int> > a(n, vector<int>(m));
	for(int i = 0; i < n; ++i) {
		for(int j = 0;j < m; ++j) {
			cin >> a[i][j];
		}
	}
	vector<int> b(n, -1), c(m, -1);
	for(int i = 0;i < n; ++i) {
		for(int j = 0;j < m; ++j) {
			b[i] = max(b[i], a[i][j]);
			c[j] = max(c[j], a[i][j]);
		}
	}
	bool possible = true;
	for(int i = 0;i < n; ++i) {
		for(int j = 0;j < m; ++j) {
			possible = possible && min(b[i], c[j]) == a[i][j];
		}
	}
	if(possible) {
		printf("Case #%d: YES\n", t);
	} else {
		printf("Case #%d: NO\n", t);
	}
}

int main() {
	int T;
	cin >> T;
	for(int i = 1;i <= T; ++i) {
		solve(i);
	}
}