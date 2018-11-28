#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <numeric>
#include <tuple>
#include <climits>

#define INF 1023456789
#define SQR(x) ((x)*(x))
#define INIT(x,y) memset((x),(y),sizeof((x)))
#define SIZE(x) ((int)((x).size()))
#define REP(i, n) for (__typeof(n) i=0;i<(n);++i)
#define FOR(i, a, b) for (__typeof(a) i=(a);i<=(b);++i)
#define FORD(i, a, b) for (__typeof(a) i=(a);i>=(b);--i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define DEBUG
#ifdef DEBUG
#define DBG(x) cerr << #x << ": " << (x) << endl;
#else
#define DBG(x)
#endif

using namespace std;
 
typedef long long LL;
typedef pair<int,int> PI;
typedef tuple<int,int,int>trio;

inline void solve(int t)
{
	printf("Case #%d: ",t);
	int r1,r2,M[10][10];
	scanf("%d",&r1);
	REP(i,4) REP(j,4) scanf("%d",&M[i][j]);
	scanf("%d",&r2);
	int ans = -1;
	--r1;--r2;
	bool ok = true;
	REP(i,4)
	{
		REP(j,4)
		{
			int num;
			scanf("%d",&num);
			if (i==r2)
			{
				REP(k,4) if (M[r1][k]==num) 
				{
					if (ans!=-1) ok = false;
					ans = num;
					break;
				}
			}
		}
	}
	if (ans==-1) printf("Volunteer cheated!\n");
	else if (!ok) printf("Bad magician!\n");
	else printf("%d\n",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	REP(i,T) solve(i+1);
        return 0;
}
