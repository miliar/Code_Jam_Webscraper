#pragma warning(disable:4996)
#include <iostream>
#include <functional>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
using namespace std;
typedef long long ll;

#define INF 0x333f3f3f
#define repp(i, n, m) for (int i = n; i <= m; i++)
#define rep(i, n, m) for (int i = n; i < m; i++)
#define sa(n) scanf("%d", &(n))

const ll mod = 100000007;
const int maxn = 105;
const double PI = acos(-1.0);

int len, dp[maxn];
char x[maxn];


void solve()
{
	int i, j, k;

	scanf("%s", x);
	len = strlen(x);
	memset(dp, 0, sizeof(dp));
	dp[0] = (x[0] == '-' ? 1 : 0);

	for (i = 1; i < len; i++)
	{
		if (x[i] == '+')
		{
			dp[i] = dp[i - 1];
		}
		else if (x[i] == '-')
		{
			if (x[i - 1] == '-')
			{
				dp[i] = dp[i - 1];
			}
			else
			{
				dp[i] = dp[i - 1] + 2;
			}
		}
	}
	printf("%d\n", dp[len - 1]);
}

int main()
{
/*	
#ifndef ONLINE_JUDGE  
	freopen("i.txt", "r", stdin);
	freopen("o.txt", "w", stdout);
#endif
*/
	int i, t;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}