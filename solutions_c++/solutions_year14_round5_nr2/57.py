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

const int MAX = 105;

int T;
int P, Q, N;
int H[MAX], G[MAX];
int dp[MAX][2005];

int DP(int i, int shots)
{
	if (shots > 2000)
		return 0;
	if (i == N)
		return 0;
	
	if (dp[i][shots] == -1)
	{
		dp[i][shots] = 0;
		
		REP(t, 11)
		{
			int hp = H[i] - t*Q;
			
			// leave
			dp[i][shots] = max(dp[i][shots], DP(i+1, shots+t));
			
			// take down
			int need = (max(0, hp) + P - 1) / P;
			if (hp > 0 && shots + t >= need)
			dp[i][shots] = max(dp[i][shots], G[i] + DP(i+1, shots+t-need));
			
			if (hp <= 0)
				break;
		}
	}
	return dp[i][shots];
}

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d %d %d", &P, &Q, &N);
		REP(i, N)
			scanf("%d %d", &H[i], &G[i]);
		
		RESET(dp, -1);
		printf("Case #%d: %d\n", tc+1, DP(0, 1));
	}
}
