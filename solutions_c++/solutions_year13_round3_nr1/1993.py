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
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
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

int main()
{
    READ("A-small-attempt0.in");
    WRITE("A-small-attempt0.out");
    int i, j, l, t, k, ret, n, sz, c, len;
    string str, vwl="aouie", tmp, add;
    scanf("%d",&t);
    rep(k,1,t+1)
    {
        cin >> str >> n;
        sz = len = SZ(str), ret=0;
        REP(i,sz-n+1)
        {
            rep(j,1,len+1)
            {
                tmp = str.substr(i,j);
                if(j<1)
                    continue;
                c=0;
                REP(l,SZ(tmp))
                {
                    if(vwl.find(tmp[l])==-1) c++;
                    else if(c>=n)
                        {c=n; break;}
                    else c=0;
                }
                if(c>=n)
                    ret++;
            }
            len--;
        }
        printf("Case #%d: %d\n",k,ret);
    }
    return 0;
}
