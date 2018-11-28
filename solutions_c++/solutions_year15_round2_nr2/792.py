#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

const int INF = 1e8;
int dp[20][20][20];

int happy;
int bits(int x)
{
	int y = 0;
	happy = 0;
	int has = 0;
	while (x > 0)
	{
		y += (x & 1);
		if ((x & 1) && has)
			happy++;
		has = (x & 1);
		x >>= 1;
	}
	return y;
}

void Solution()
{
	int n, r, c;
	cin >> r >> c >> n;
	if (c > r)
		swap(r, c);

	for (int i = 0; i < 20; i++)
		for (int j = 0; j < 20; j++)
			for (int k = 0; k < 20; k++)
				dp[i][j][k] = INF;
	
	dp[0][0][0] = 0;
	int all = (1 << c) - 1;
	for (int i = 0; i < r; i++)
		for (int mask = 0; mask <= all; mask++)
			for (int mans = 0; mans <= n; mans++)
			{
				if (dp[i][mask][mans] == INF)
					continue;
				for (int mask2 = 0; mask2 <= all; mask2++)
				{
					int mans2 = mans + bits(mask2);
					int val2 = dp[i][mask][mans] + happy + bits((mask & mask2));
					dp[i + 1][mask2][mans2] = min(dp[i + 1][mask2][mans2], val2);
				}
			}

	int ans = INF;
	for (int mask = 0; mask <= all; mask++)
		ans = min(ans, dp[r][mask][n]);
	cout << ans;
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}