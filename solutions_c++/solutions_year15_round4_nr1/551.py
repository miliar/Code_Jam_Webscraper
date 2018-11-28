#include<cstdio>
#include<cstring>
#define MAXN 110
char mp[MAXN][MAXN];
bool f[MAXN][MAXN];
int n, m;
bool isOut(int x, int y) {
	if (mp[x][y] == '.') {
		return false;
	}
	if (mp[x][y] == '>') {
		for (int j = y + 1; j < m; j++) {
			if (mp[x][j] != '.') {
				return false;
			}
		}
	} else if (mp[x][y] == 'v') {
		for (int i = x + 1; i < n; i++) {
			if (mp[i][y] != '.') {
				return false;
			}
		}
	} else if (mp[x][y] == '^') {
		for (int i = x - 1; i >= 0; i--) {
			if (mp[i][y] != '.') {
				return false;
			}
		}
	} else if (mp[x][y] == '<') {
		for (int i = y - 1; i >= 0; i--) {
			if (mp[x][i] != '.') {
				return false;
			}
		}
	}
	return true;
}
bool isOut4(int x, int y) {
	for (int j = y + 1; j < m; j++) {
		if (mp[x][j] != '.') {
			return false;
		}
	}
	for (int i = x + 1; i < n; i++) {
		if (mp[i][y] != '.') {
			return false;
		}
	}
	for (int i = x - 1; i >= 0; i--) {
		if (mp[i][y] != '.') {
			return false;
		}
	}
	for (int i = y - 1; i >= 0; i--) {
		if (mp[x][i] != '.') {
			return false;
		}
	}
	return true;
}
bool isOK() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (f[i][j]) {
				if (isOut4(i, j)) {
					return false;
				}
			}
		}
	}
	return true;
}
int main() {
	int T;
	int ca = 1;
	freopen("in", "r", stdin);
	freopen("r2", "w", stdout);
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf(" %c", &mp[i][j]);
			}
		}
		int ans = 0;
		memset(f, false, sizeof(f));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (isOut(i, j)) {
					f[i][j] = true;
					++ans;
				}
			}
		}
		if (isOK()) {
			printf("Case #%d: %d\n", ca++, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", ca++);
		}
	}
	return 0;
}
