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

const int oo = 999999999;

int T;
int N, A[1005];
pair<int, int> P[1005];
int le[1005][1005];
int dp[1005];
int pos[1005];

int DP(int i)
{
	if (i == N)
		return 0;
	
	if (dp[i] == -1)
	{
		int cur = pos[i] - le[pos[i]][i];
		dp[i] = DP(i+1) + min(cur, N-i-cur-1);
	}
	return dp[i];
}


int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d", &N);
		REP(i, N)
		{
			scanf("%d", &P[i].first);
			P[i].second = i;
		}
		sort(P, P+N);
		REP(i, N)
			A[P[i].second] = i;
		
		REP(i, N)
			pos[A[i]] = i;
		
		RESET(dp, -1);
		RESET(le, 0);
		
		REP(i, N)
		{
			FOR(j, 1, N)
			{
				le[i][j] += le[i][j-1];
				if (pos[j-1] < i)
					le[i][j]++;
			}
		}
		
		
		printf("Case #%d: %d\n", tc+1, DP(0));
	}
}
