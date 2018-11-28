#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <set>
#include <map>
#include <list>
#include <queue>
#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T, N, M;
int lawn[100][100];
int maxr[100];
int maxc[100];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	REP(tc, T)
	{
		RESET(lawn, 0);
		RESET(maxr, 0);
		RESET(maxc, 0);
		cin >> N >> M;
		REP(i, N)
		{
			REP(j, M)
			{
				cin >> lawn[i][j];
				if (lawn[i][j] > maxr[i]) maxr[i] = lawn[i][j];
				if (lawn[i][j] > maxc[j]) maxc[j] = lawn[i][j];
			}
		}
		bool can = true;
		REP(i, N)
		{
			REP(j, M)
			{
				if (lawn[i][j] < maxr[i] && lawn[i][j] < maxc[j]) 
				{
					can = false;
					break;
				}
			}
		}
		printf("Case #%d: %s\n", tc+1, can ? "YES" : "NO");
	}
}