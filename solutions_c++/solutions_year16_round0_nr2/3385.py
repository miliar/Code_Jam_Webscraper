#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define N 1000

int dp[N][2];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("dataB.out","w",stdout);
	char str[N];
	int T, ys = 0;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%s", str);
		int n = strlen(str);
		dp[0][0] = (str[0] == '-') ? 0 : 1;
		dp[0][1] = (str[0] == '+') ? 0 : 1;
		for (int i = 1; i < n; ++i)
			if (str[i] == '-')
			{
				dp[i][0] = dp[i-1][0];
				dp[i][1] = dp[i-1][0] + 1;
			}
			else
			{
				dp[i][0] = dp[i-1][1] + 1;
				dp[i][1] = dp[i-1][1];
			}
		printf("Case #%d: ", ++ys);
		printf("%d\n", dp[n-1][1]);
	}

	return 0;
}
