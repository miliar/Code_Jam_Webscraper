#include <bits/stdc++.h>
using namespace std;
int arr[105];
char foo[105];
int dp[105][105][2][2];
int moves(int p, int q, int rev, int to)
{
	if(p> q) return 0;
	if(p == q)
	{
		if(arr[p] == to) return 0;
		return 1;
	}
	int all1 = 1;
	int all0 = 1;
	if(dp[p][q][rev][to] != -1) return dp[p][q][rev][to];
	for(int i= p; i<= q; i++)
	{
		if(!arr[i]) all1 = 0;
		if(arr[i]) all0 =0;
	}
	if(to && all1) return 0;
	if(!to && all0) return 0;
	int ans = 1e9;
	int til;
	if(rev == 0)
	{
		til = q;
		if(arr[q] == to)
		for(int i = q; i>= p; i--)
		{
			if(arr[i] != to)
			{
				til = i;
				break;
			}
		}
		if(p == til)
		{
			if(arr[p] == to) return 0;
			return 1;
		}
		for(int i = p; i< til; i++)
		{
			ans = min(ans, moves(p, i, rev, 1-to) + moves(i+1, til, 1-rev, 1-to));	
		}
		return dp[p][q][rev][to] = ans+1;
	}
	else
	{
		til = p;
		if(arr[p] == to)
		for(int i = p; i<= q; i++)
		{
			if(arr[i] != to)
			{
				til = i;
				break;
			}
		}
		if(q == til)
		{
			if(arr[q] == to) return 0;
			return 1;
		}
		for(int i = q; i> til; i--)
		{
			ans = min(ans, moves(i, q, rev, 1-to) + moves(til, i-1, 1-rev, 1-to));
		}
		return dp[p][q][rev][to] = ans+1;
	}
}
int main()
{
	int tt;
	freopen("inlarge", "r", stdin);
	freopen("outlarge", "w", stdout);
	scanf("%d", &tt);
	for(int qq = 1; qq<= tt; qq++)
	{
		memset(dp, -1, sizeof dp);
		scanf("%s", foo);
		int n = strlen(foo);
		printf("Case #%d: ", qq);
		for(int i= 0; i< n; i++)
		{
			arr[i] = (foo[i] == '+');
		}
		printf("%d\n", moves(0, n-1, 0, 1));
	}
}