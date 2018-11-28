#include <bits/stdc++.h>
using namespace std;

int dp[1001][1001];
int arr[1001];

inline void set_min(int &var, int val)
{
	if (var == -1)
		var = val;
	else
		var = min(var, val);
}

int main()
{
	int T, D, mx, ans;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		for (int i = 0; i < 1001; i++)
			for (int j = 0; j < 1001; j++)
				dp[i][j] = -1;
		dp[0][0] = 0;
		
		scanf("%d", &D);
		mx = 0;
		for (int i = 0; i < D; i++)
		{
			scanf("%d", arr + i);
			mx = max(arr[i], mx);
		}

		for (int i = 0; i < D; i++)
		{
			int d = arr[i];
			for (int j = 0; j < mx; j++)
			{
				if (dp[i][j] == -1)
					continue;
				
				set_min(dp[i + 1][j], max(d, dp[i][j]));
				if (d > 3)
				{
					for (int k = 1; k * k <= d && j + k < mx; k++)
						set_min(dp[i + 1][j + k], max(((d - 1) / (k + 1)) + 1, dp[i][j]));
				}
			}
		}

		ans = mx;
		for (int i = 0; i < mx; i++)
			if (dp[D][i] != -1)
				ans = min(dp[D][i] + i, ans);

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}