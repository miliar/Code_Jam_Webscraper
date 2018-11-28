#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>

using namespace std;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) (x).size()
#define MMS(x,n) memset(x,n,sizeof(x))
#define pb push_back
#define mp make_pair
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int arr[101][101];

int main()
{
    READ("B-large.in");
    WRITE("B-large.out");
    int i, j, t, k, n, m, u;
    bool ver, hor, ans;
    scanf("%d",&t);
    rep(k,1,t+1)
    {
        MMS(arr,0);
        scanf("%d %d",&n,&m);
        ans = 1;
        REP(i,n) REP(j,m) scanf("%d",&arr[i][j]);
        REP(i,n) REP(j,m)
        {
            ver = hor = 0;
            REP(u,n) if(arr[u][j]>arr[i][j]) { ver=1; break; }
            REP(u,m) if(arr[i][u]>arr[i][j]) { hor=1; break; }
            if(ver && hor) { ans=0; goto end; }
        }
        end:
        if(ans)
            printf("Case #%d: YES\n",k);
        else
            printf("Case #%d: NO\n",k);
    }
    return 0;
}
