#include <bits/stdc++.h>

using namespace std;

int n, m, cc[111], cr[111];
char s[111][111];

vector<pair<int, int> > bad;

void solve() {
	for (int i = 0; i < 111; i++) cc[i] = cr[i] = 0;
	bad.clear();
	
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) {
		scanf("%s", s[i]+1);
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (s[i][j] != '.') cc[j]++, cr[i]++;
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (s[i][j] == '<') bad.push_back(make_pair(i, j));
			if (s[i][j] != '.') break;
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = m; j >= 0; j--) {
			if (s[i][j] == '>') bad.push_back(make_pair(i, j));
			if (s[i][j] != '.') break;
		}
	}
	for (int j = 1; j <= m; j++) {
		for (int i = 1; i <= n; i++) {
			if (s[i][j] == '^') bad.push_back(make_pair(i, j));
			if (s[i][j] != '.') break;
		}
	}
	for (int j = 1; j <= m; j++) {
		for (int i = n; i >= 1; i--) {
			if (s[i][j] == 'v') bad.push_back(make_pair(i, j));
			if (s[i][j] != '.') break;
		}
	}
	for (int i = 0; i < int(bad.size()); i++) {
		int x = bad[i].first, y = bad[i].second;
		if (cr[x] == 1 && cc[y] == 1) {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", int(bad.size()));
}

int main() {
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}