#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <functional>
#include <queue>
using namespace std;
const double ZERO = 1e-6;

int main()
{
//	freopen("sample.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d\n", &t);
	for(int i = 1; i <= t; i++)
	{
		double c, f, x;
		scanf("%lf %lf %lf\n", &c, &f, &x);
		printf("Case #%d: ", i);
		//int p = 2;
		vector<double> dp(3, 0.0);
		dp[1] = 2;
		dp[2] = x / dp[1];

		while(true)
		{
			dp[0] += c / dp[1];
			dp[1] += f;
			double val = dp[0] + x / dp[1];
			if(dp[2] < val)
			{
				printf("%.7lf\n", dp[2]);
				break;
			}
			dp[2] = val;
		}
	}

    return 0;
}