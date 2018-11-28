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

const int sz = 1e5 + 100;
double dp[sz];

void Solution()
{
	double cost, mine, goal;
	cin >> cost >> mine >> goal;

	dp[0] = 0;
	for (int i = 1; i < sz; i++)
	{
		dp[i] = dp[i - 1] + cost / (2.0 + mine * (i - 1.0));
	}

	double ans = 1e18;
	for (int i = 0; i < sz; i++)
	{
		double loc = dp[i] + goal / (2.0 + mine * i);
		ans = min(ans, loc);
	}
	printf("%.9lf", ans);
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