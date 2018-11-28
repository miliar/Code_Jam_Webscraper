#include <cstdio>

int T, n, m, a[4][4], b[4][4];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);
		scanf("%d", &m);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) scanf("%d", &b[i][j]);
		int ans = -1, cnt = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				if (a[n - 1][i] == b[m - 1][j]) {
					ans = a[n - 1][i];
					cnt++;
					break;
				}
			}
		printf("Case #%d: ", t);
		if (cnt == 1) printf("%d\n", ans);
		else if (cnt == 0) puts("Volunteer cheated!");
		else puts("Bad magician!");
	}
}