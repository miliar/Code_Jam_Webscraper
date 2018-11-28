/* by Ashar Fuadi (fushar) */

#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T;
int N, X;
char op[15];
int id[15];
bool seen[2005];
int compressed[2005];
int dp[17][1<<17];

int DP(int i, int mask)
{
	if (i == N)
		return __builtin_popcount(mask);
	
	if (dp[i][mask] == -1)
	{
		dp[i][mask] = 999999999;
		if (op[i] == 'E')
		{
			REP(j, N+1) if (j && (id[i] == 0 || id[i] == j) && !(mask & (1<<j)))
				dp[i][mask] = min(dp[i][mask], DP(i+1, mask | (1<<j)));
		}
		else
		{	
			REP(j, N+1) if (j && (id[i] == 0 || id[i] == j) && (mask & (1<<j)))
				dp[i][mask] = min(dp[i][mask], DP(i+1, mask ^ (1<<j)));
		}
	}
	return dp[i][mask];
}

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		RESET(seen, false);
		scanf("%d", &N);
		REP(i, N)
		{
			char s[10];
			int x;
			scanf("%s %d", s, &x);
			op[i] = s[0];
			id[i] = x;
			seen[x] = true;
		}
		seen[0] = true;
		X = 0;
		REP(i, 2001) if (seen[i])
			compressed[i] = X++;
		
		REP(i, N)
			id[i] = compressed[id[i]];
		
		RESET(dp, -1);
		int ans = 999999999;
		REP(mask, 1<<(N+1)) if (!(mask & 1))
			ans = min(ans, DP(0, mask));
		if (ans == 999999999)
			printf("Case #%d: CRIME TIME\n", tc+1);
		else
			printf("Case #%d: %d\n", tc+1, ans);
	}
}
