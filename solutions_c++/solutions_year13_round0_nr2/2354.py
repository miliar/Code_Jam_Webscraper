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

const int MAX = 105;
int T, N, M, A[MAX][MAX];
bool mowed[MAX][MAX];

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%d", &N, &M);
		REP(i, N) REP(j, M)
			scanf("%d", &A[i][j]);
		
		RESET(mowed, false);
		FOR(h, 1, 100)
		{
			// row
			REP(i, N)
			{
				bool found = true;
				bool any = false;
				
				REP(j, M)
				{
					if (A[i][j] > h || (A[i][j] < h && !mowed[i][j]))
					{
						found = false;
						break;
					}
					
					if (A[i][j] == h && !mowed[i][j])
						any = true;
				}
				
				if (found && any)
				{
					REP(j, M)
						mowed[i][j] = true;
				}
			}
			// column
			REP(j, M)
			{
				bool found = true;
				bool any = false;
				
				REP(i, N)
				{
					if (A[i][j] > h || (A[i][j] < h && !mowed[i][j]))
					{
						found = false;
						break;
					}
					
					if (A[i][j] == h && !mowed[i][j])
						any = true;
				}
				
				if (found && any)
				{
					REP(i, N)
						mowed[i][j] = true;
				}
			}
		}
		
		int numMowed = 0;
		REP(i, N) REP(j, M)
			numMowed += mowed[i][j];
		
		printf("Case #%d: %s\n", tc+1, numMowed == N * M ? "YES" : "NO");
	}
}
