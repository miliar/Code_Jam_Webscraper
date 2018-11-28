#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

const int MAX_N = 105;
int dp[MAX_N][MAX_N][1105];
int n, p, q;
int h[MAX_N], g[MAX_N];
int a[MAX_N], b[MAX_N];

inline void checkMax(int &a, int b) { if (a < b) a = b; }

int main() {
	int n_case = 0;
	scanf("%d", &n_case);
	for (int ca = 1; ca <= n_case; ca++) {
		scanf("%d%d%d", &p, &q, &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d%d", h + i, g + i);
			a[i] = (h[i] - 1) / q;
			b[i] = (h[i] - a[i] * q + p - 1) / p;
		}
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= i; j++) {
				for (int k = 0; k <= i * 11 + 1; k++) {
					dp[i][j][k] = -100;
				}
			}
		}
		dp[0][0][1] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				for (int k = 0; k <= i * 11 + 1; k++) {
					if (dp[i][j][k] < 0) continue;
					if (k >= b[i + 1] - a[i + 1]) {
						checkMax(dp[i + 1][j + 1][k - b[i + 1] + a[i + 1]], dp[i][j][k] + g[i + 1]);
					}
					checkMax(dp[i + 1][j][k + a[i + 1] + 1], dp[i][j][k]);
				}
			}
		}
		int ans = 0;
		for (int j = 0; j <= n; j++) {
			for (int k = 0; k <= n * 11 + 1; k++) {
				checkMax(ans, dp[n][j][k]);
			}
		}
		fprintf(stderr, "Case #%d: %d\n", ca, ans);
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}
