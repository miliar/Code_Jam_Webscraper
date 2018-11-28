/* by Ashar Fuadi (fushar) */

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T, N;
int keyToOpen[25];
int keysInside[25][45], K[25];

int currentKeys[205];
bool dp[1<<20];
int next[1<<20];

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		RESET(keyToOpen, 0);
		RESET(keysInside, 0);
		
		scanf("%d%d", &K[0], &N);
		REP(i, K[0])
			scanf("%d", &keysInside[0][i]);
			
		FOR(i, 1, N)
		{
			scanf("%d", &keyToOpen[i]);
			scanf("%d", &K[i]);
			REP(j, K[i])
				scanf("%d", &keysInside[i][j]);
		}
		
		RESET(dp, false);
		dp[(1<<N)-1] = true;
		for (int mask = (1<<N)-2; mask >= 0; mask--)
		{
			RESET(currentKeys, 0);
			REP(i, K[0])
				currentKeys[keysInside[0][i]]++;
			
			REP(i, N) if (mask & (1<<i))
			{
				currentKeys[keyToOpen[i+1]]--;
				REP(j, K[i+1])
					currentKeys[keysInside[i+1][j]]++;
			}
			
			for (int i = N-1; i >= 0; i--) if (!(mask & (1<<i)))
				if (currentKeys[keyToOpen[i+1]] > 0 && dp[mask | (1<<i)])
				{
					dp[mask] = true;
					next[mask] = i;
				}
		}
		
		printf("Case #%d:", tc+1);
		if (!dp[0])
			printf(" IMPOSSIBLE\n");
		else
		{
			int mask = 0;
			while (mask != (1<<N)-1)
			{
				printf(" %d", next[mask]+1);
				mask = mask | (1<<next[mask]);
			}
			printf("\n");
		}
	}
}
