#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 110;

int H[N], G[N];
int K[N], T[N], OT[N], more[N];

int dp[N][20010];

int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int TT; scanf("%d", &TT);
	for (int kase = 1; kase <= TT; kase++)
	{
		int P, Q, n; scanf("%d %d %d", &P, &Q, &n);
		// printf("P = %d, Q = %d\n", P, Q);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d %d", &H[i], &G[i]);
			OT[i] = (H[i] + Q - 1) / Q;
			K[i] = -1;
			for (int k = 1; K[i] == -1; k++)
			{
				for (int t = OT[i]; t >= 0; --t)
				{
					if ((k - 1) * P + t * Q < H[i] && k * P + t * Q >= H[i])
					{
						K[i] = k, T[i] = t;
						break;
					}
				}
			}
			more[i] = T[i] - K[i];
			// printf("[%d %d] OT %d = %d, more %d (K = %d, T = %d) = %d\n", H[i], G[i], i, OT[i], i, K[i], T[i], more[i]);
		}
		memset(dp, -1, sizeof dp);
		dp[0][1] = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < 20010; j++) if (dp[i][j] != -1)
			{
				// printf("DP %d %d = %d\n", i, j, dp[i][j]);
				if (j + OT[i + 1] < 20010) dp[i + 1][j + OT[i + 1]] = max(dp[i + 1][j + OT[i + 1]], dp[i][j]);
				else if (j + OT[i + 1] >= 20010) printf("WARNING!!!\n");
				if (j + more[i + 1] >= 0 && j + more[i + 1] < 20010) dp[i + 1][j + more[i + 1]] = max(dp[i + 1][j + more[i + 1]], dp[i][j] + G[i + 1]);
			}
		}
		int ans = -1;
		for (int j = 0; j < 20010; j++)
		{
			// if (dp[n][j] != -1) printf("DP %d %d = %d\n", n, j, dp[n][j]);
			ans = max(ans, dp[n][j]);
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	fclose(stdin), fclose(stdout);
	return 0;
}
