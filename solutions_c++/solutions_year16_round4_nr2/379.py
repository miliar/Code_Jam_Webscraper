#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<numeric>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<list>
#include<cmath>
#include<bitset>
#include<cassert>
#include<queue>
#include<stack>
#include<deque>
#include<cassert>
using namespace std;
typedef long long ll;
typedef long double ld;
double dp[207][207];
double calc(int n, vector<double>p)
{
	for (int i = 0; i <= n + 1; i++)
	{
		for (int j = 0; j <= n + 1; j++)
		{
			dp[i][j] = 0;
		}
	}
	dp[0][0] = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= n; j++)
		{
			dp[i + 1][j + 1] += dp[i][j] * p[i];
			dp[i + 1][j] += dp[i][j] * (1 - p[i]);
		}
	}
	return dp[n][n / 2];
}
double p[207];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << tt << endl;
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 1; i <= n; i++)
		{
			scanf("%lf", &p[i]);
		}
		sort(p + 1, p + 1 + n);
		double res2 = 0;
		for (int i = 0; i <= k; i++)
		{
			vector<double>go;
			for (int j = 1; j <= i; j++)
			{
				go.push_back(p[j]);
			}
			int more = k - i;
			for (int j = n - more + 1; j <= n; j++)
			{
				go.push_back(p[j]);
			}
			res2 = max(res2, calc(k, go));
		}
		printf("Case #%d: %.10lf\n", tt, res2);
	}
}
