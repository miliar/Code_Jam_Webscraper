#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

const int N = 205;
double pp[N];
double p[N];
double dp[N][N];

void solve()
{
	int n, k;
	scanf("%d%d", &n, &k);
	
	for (int i = 0; i < n; i++)
	{
		int x, y;
		scanf("%d.%d", &x, &y);
		pp[i] = x + y / 100.0;
	}

	double ans = 0;
	
	for (int mask = 0; mask < (1 << n); mask++)
	{
		int m = 0;
		for (int i = 0; i < n; i++)
		{
			if (mask & (1 << i))
			{
				p[m++] = pp[i];
			}
		}
		if (m != k)
			continue;

		for (int i = 0; i <= m; i++)
			for (int j = 0; j <= m; j++)
				dp[i][j] = 0;
		dp[0][0] = 1;

		for (int i = 0; i < m; i++)
			for (int j = 0; i + j < m; j++)
			{
				dp[i + 1][j] += dp[i][j] * p[i + j];
				dp[i][j + 1] += dp[i][j] * (1 - p[i + j]);
			}

		ans = max(ans, dp[k / 2][k / 2]);
	}

	printf("%.15lf", ans);
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
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}