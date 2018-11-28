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

int cnt;
LL V[10000047];

inline bool palindrome(LL x)
{
        string str=to_string(x);
        string rev=str;
        reverse(rev.begin(),rev.end());
        return rev==str;
}

int main()
{
        cnt=0;
        REP(i,10000047LL)
        {
                LL x=SQR(i);
                if (palindrome(i) && palindrome(x)) V[cnt++]=x;
        }
        int T;
        scanf("%d",&T);
        REP(i,T)
        {
                LL a,b;
                scanf("%lld%lld",&a,&b);
                int res(0);
                REP(j,cnt) if (V[j]>=a && V[j]<=b) res++;
                printf("Case #%d: %d\n",i+1,res);
        }
        return 0;
}
