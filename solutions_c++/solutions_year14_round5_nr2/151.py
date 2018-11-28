#include <cstdio>
#include <algorithm>
using namespace std;

const int Maxn = 105;
const int Maxm = 2005;
const int Inf = 2000000000;

int t;
int p, q, n;
int h[Maxn], g[Maxn];
int dp[Maxn][2][Maxm];
int mn[Maxn], hits[Maxn];

void Kill(int hp, int &hs, int &lft)
{
	hs = (hp - 1) / q; lft = hp - hs * q;
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d", &p, &q, &n);
		for (int i = 0; i <= n; i++)
			for (int k = 0; k < 2; k++)
				for (int j = 0; j < Maxm; j++)
					dp[i][k][j] = -Inf;
		dp[0][0][0] = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &h[i], &g[i]);
			int j;
			for (j = 0; p * j < h[i]; j++) {
				int hs, lft; Kill(h[i] - p * j, hs, lft);
				if (lft <= p) { mn[i] = j; hits[i] = hs; break; }
			}
			if (p * j >= h[i]) mn[i] = Inf;
			for (int j = 0; j < 2; j++)
				for (int hm = 0; hm < Maxm; hm++) if (dp[i][j][hm] >= 0) {
					int hs = (h[i] - 1) / q + 1;
					dp[i + 1][0][hm + hs - j] = max(dp[i + 1][0][hm + hs - j], dp[i][j][hm]);
					if (mn[i] != Inf) {
						int reser = hits[i] + 1 - j;
						if (reser + hm >= mn[i] + 1)
							dp[i + 1][1][reser + hm - mn[i] - 1] = max(dp[i + 1][1][reser + hm - mn[i] - 1], dp[i][j][hm] + g[i]);
					}
				}
		}
		int res = -Inf;
		for (int k = 0; k < 2; k++)
			for (int j = 0; j < Maxm; j++)
				res = max(res, dp[n][k][j]);
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}