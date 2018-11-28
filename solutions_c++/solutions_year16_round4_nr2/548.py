#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
double pra[10000];
vector<double>ans_arr;
double dp[300][300];
int main()
{
	int T; cin >> T;
	for (int TT = 1; TT <= T; ++TT)
	{
		printf("Case #%d: ", TT);
		int n, k; cin >> n >> k;
		for (int i = 0; i < n; ++i)
		{
			cin >> pra[i];
		}
		sort(pra, pra + n);
		double ans = 0;
		for (int i = 0; i <= k; ++i)
		{
			ans_arr.clear();
			for (int j = 0; j < i; ++j)
			{
				ans_arr.push_back(pra[j]);
			}
			for (int j = n - (k - i); j < n; ++j)
			{
				ans_arr.push_back(pra[j]);
			}
			dp[1][0] = 1-ans_arr[0];
			dp[1][1] = ans_arr[0];
			for(int j=2;j<=k;++j)
			{
				for(int m=0;m<=j;++m)
				{
					dp[j][m] = dp[j-1][m] * (1 - ans_arr[j-1]);
					if(m > 0) dp[j][m] += dp[j-1][m - 1] * ans_arr[j-1];
				}
			}
			ans = max(ans, dp[k][k/2]);
		}
		printf("%f\n",ans);
	}
	return 0;
}
