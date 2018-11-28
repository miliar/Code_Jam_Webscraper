#include <cstdio>

#define N 128
#define M 1024

int max(int a, int b) {
	return a < b ? b : a;
}

int T, p, q, n, h, x[N], y[N], g[N], dp[N][M], ans;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d%d", &p, &q, &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &h, g + i);
			x[i] = (h + q - 1)/q;
			y[i] = x[i] - 2 - (h - 1)%q/p;
		}
		for (int i = 0; i <= n; ++i)
			for (int j = 0; j < M; ++j)
				dp[i][j] = -1 << 28;
		dp[0][1] = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < M; ++j)
				if (dp[i][j] >= 0) {
					dp[i + 1][j + x[i]] = max(dp[i + 1][j + x[i]], dp[i][j]);
					if (j + y[i] >= 0)
						dp[i + 1][j + y[i]] = max(dp[i + 1][j + y[i]], dp[i][j] + g[i]);
				}
		ans = 0;
		for (int j = 0; j < M; ++j)
			ans = max(ans, dp[n][j]);
		printf("%d\n", ans);
	}
	return 0;
}
