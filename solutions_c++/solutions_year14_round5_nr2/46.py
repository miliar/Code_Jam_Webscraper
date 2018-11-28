#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;


const int maxn = 105;
int h[maxn], g[maxn];

const int maxq = maxn * 210;
int dp[maxn][maxq];


void getSome(int h, int p, int q, int &a, int &b)
{
	b = h / q;
	int curh = h - b * q;
	if (curh == 0)
	{
		b--;
		curh += q;
	}
	a = (curh + p - 1) / p;
}


void solve()
{
	int p, q, n;
	scanf("%d%d%d", &p, &q, &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &h[i], &g[i] );
	}
	memset(dp, -1, sizeof dp);
	dp[0][1] = 0;
	for (int i = 0; i < n; i++)
	{
		int tower = (h[i] + q - 1) / q;
		
		int needFire = 0;
		int altTower = 0;
		getSome(h[i], p, q, needFire, altTower);


	//	fprintf(stderr, "tower = %d, needFire = %d, altTower = %d\n", tower, needFire, altTower);

		for (int j = 0; j <= 205 * i + 1; j++)
		{
			int curdp = dp[i][j];
			if (curdp == -1)
				continue;
			
			dp[i + 1][j + tower] = max(dp[i + 1][j + tower], curdp);
			
			int nj = j + altTower - needFire;
		//	fprintf(stderr, "nj = %d\n", nj);
			if (nj < 0)
				continue;
		//	fprintf(stderr, "!!!");
			dp[i + 1][nj] = max(dp[i + 1][nj], curdp + g[i] );
		}
	}
	int ans = 0;
	for (int j = 0; j < maxq; j++)
		ans = max(ans, dp[n][j] );
	printf("%d", ans);

}



int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		fprintf(stderr, "Case #%d: ", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
		fprintf(stderr, "OK\n");
	}


	return 0;
}