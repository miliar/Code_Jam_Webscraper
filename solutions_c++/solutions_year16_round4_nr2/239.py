#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
double dp[202][202];
int n, k;
double p[202];
int main()
{
	int T, cas = 0;
	freopen("in.txt", "r", stdin);
	freopen("out2.txt", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; i++)
			scanf("%lf", &p[i]);
		sort(p, p + n);
		double res = 0;
		for(int i = 0; i <= k; i++)
		{
			for(int j = 0; j <= k; j++)
				for(int l = 0; l <= k; l++)
					dp[j][l] = 0.0;
			vector<double> v;
			int need = k - i;
			for(int j = 0; j < i; j++)
				v.push_back(p[j]);
			for(int j = n - need; j < n; j++)
				v.push_back(p[j]);
			dp[0][1] = v[0];
			dp[0][0] = 1 - v[0];
			for(int j = 0; j < k - 1; j++)
				for(int l = 0; l <= k / 2; l++)
				{
					dp[j + 1][l] += dp[j][l] * (1 - v[j + 1]);
					dp[j + 1][l + 1] += dp[j][l] * v[j + 1];
				}
			res = max(res, dp[k - 1][k / 2]);
		}
		printf("Case #%d: %.10f\n", ++cas, res);
	}
}