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

int a[147][147],row[147],col[147];

inline void solve(int t)
{
        int N,M;
        scanf("%d%d",&N,&M);
        INIT(row,0);
        INIT(col,0);
        REP(i,N) 
        {
                REP(j,M)
                {
                        scanf("%d",&a[i][j]);
                        row[i]=max(row[i],a[i][j]);
                }
        }
        REP(i,M) REP(j,N) col[i]=max(col[i],a[j][i]);
        REP(i,N) REP(j,M) if (row[i]>a[i][j] && col[j]>a[i][j]) 
        {
                printf("Case #%d: NO\n",t);
                return;
        }
        printf("Case #%d: YES\n",t);
}

int main()
{
        int T;
        scanf("%d",&T);
        REP(i,T) solve(i+1);
        return 0;
}
