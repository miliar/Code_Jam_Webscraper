#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int t, n, m;
char s[120][120];
int a[120][120];
char c[10] = "^>v<";
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
bool in(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < m;
}
int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		memset(a, 0, sizeof a);
		int ans = 0, fail = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				for (int k = 0; k < 4; k++) {
					int nx = i;
					int ny = j;
					int t = 0;
					nx += dx[k];
					ny += dy[k];
					while (in(nx, ny)) {
						if (s[nx][ny] != '.') {
							a[i][j] = 1;
							t = 1;
						}
						nx += dx[k];
						ny += dy[k];
					}
					if (c[k] == s[i][j]) {
						if (!t) {
							ans += 1;
						}
					}
				}
				if (a[i][j] == 0 && s[i][j] != '.') {
					fail = 1;
				}
			}
		}
		if (fail) {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		} else {
			printf("Case #%d: %d\n", tt, ans);
		}
	}
	return 0;
}