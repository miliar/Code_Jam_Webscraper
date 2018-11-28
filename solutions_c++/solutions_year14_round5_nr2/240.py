#include <cstdio>
#include <algorithm>
using namespace std;
#define N 123

int t, n, usdmg, tdmg, h[N], g[N], th[N], req[N], dp[N][20*N];
int main() {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d", &usdmg, &tdmg, &n);
		int ans = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d %d", h+i, g+i);
			th[i] = (h[i] + tdmg-1)/tdmg;
			req[i] = (h[i] - tdmg*(th[i]-1) + usdmg-1)/usdmg;
			//printf("%d %d %d %d\n", tc, i, th[i], req[i]);
		}
		for (int i = 0; i <= n; i++) for (int j = -10*n; j < 10*n; j++) dp[i][j + 10*n] = -999999999;
		dp[0][10*n] = 0;
		for (int i = 0; i < n; i++) for (int j = -10*n; j < 10*n; j++) {
			ans = max(ans, dp[i][j + 10*n]);
			dp[i+1][j + th[i] + 10*n] = max(dp[i+1][j + th[i] + 10*n], dp[i][j + 10*n]);
			if (j >= req[i] - th[i]) dp[i+1][j - req[i] + th[i] - 1 + 10*n] = max(dp[i+1][j - req[i] + th[i] - 1 + 10*n], dp[i][j + 10*n] + g[i]);
		}
		for (int j = -10*n; j < 10*n; j++) ans = max(ans, dp[n][j + 10*n]);
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}