#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, k;
double p[200];
double dp[1 << 16][16];

int bcnt(int a)
{
	int r = 0;
	while (a)
	{
		r += a & 1;
		a >>= 1;
	}
	return r;
}

int bpos(int a)
{
	for (int i = 16; i >= 0; i--)
	{
		if (a&(1 << i)) return i;
	}
	return -1;
}

double solve()
{
	double ans = 0;
	for (int i = 1; i < 1 << n; i++)
	{
		int cnt = bcnt(i);
		if (cnt == 1)
		{
			int j = bpos(i);
			dp[i][0] = 1 - p[j];
			dp[i][1] = p[j];
		}
		else if (cnt > k) continue;
		else
		{
			int l = i - (i&-i);
			int j = bpos(i&-i);
			dp[i][0] = dp[l][0] * (1 - p[j]);
			dp[i][cnt] = dp[l][cnt - 1] * p[j];
			for (int a = 1; a < cnt; a++)
			{
				dp[i][a] = dp[l][a] * (1 - p[j]) + dp[l][a - 1] * p[j];
			}
			if (cnt == k)
			{
				if (dp[i][k / 2] > ans) ans = dp[i][k / 2];
			}
		}
	}
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
		{
			scanf("%lf", p + i);
		}
		for (int i = 0; i < 1 << n; i++)
			for (int j = 0; j < 16; j++) dp[i][j] = 0;
		printf("Case #%d: %lf\n", t, solve());
	}
}