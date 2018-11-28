#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <string>
#include <set>

using namespace std;

string a[10];
int f[10];
set<string> st[4];
int m, n;
int ans;
int time;

void dfs(int d) {
	if (d == m) {
		for (int i = 0; i < n; i++)
			st[i].clear();

		int c = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j <= a[i].length(); j++) {
				st[f[i]].insert(a[i].substr(0, j));
				int p = 1;
			}
		}
		for (int i = 0; i < n; i++)
			c += st[i].size();
		if (c > ans) {
			ans = c;
			time = 1;
		} else if (c == ans)
			time++;
		return;
	}
	for (int i = 0; i < n; i++) {
		f[d] = i;
		dfs(d + 1);
	}
}

void work() {
	cin >> m >> n;
	for (int i = 0; i < m; i++)
		cin >> a[i];
	ans = -1;
	dfs(0);
	cout << ans << " " << time << endl;
}

int main() {
	freopen("G:/1.in", "r", stdin);
	freopen("G:/1.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		work();
		cerr << i << endl;
	}

	return 0;
}
