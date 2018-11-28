#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

typedef double dbl;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<dbl,dbl> pdd;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<dbl> vd;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<pii> vp;

#define eps 1e-9
#define inf 1000000000
#define infll 1000000000000000000LL
#define infdbl 1e15
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define sz(x) ((int)(x).size())
#define intclz(x) __builtin_clz(x)
#define intctz(x) __builtin_ctz(x)
#define intln(x) (32-intclz(x))
#define intbc(x) __builtin_popcount(x)
#define llclz(x) __builtin_clzll(x)
#define llctz(x) __builtin_ctzll(x)
#define llln(x) (64-llclz(x))
#define llbc(x) __builtin_popcountll(x)
#define atbit(x,i) (((x)>>(i))&1)
#define tof(x) __typeof(x)
#define FORab(i,a,b) for (int i=(a); i<=(b); ++i)
#define RFORab(i,a,b) for (int i=(a); i>=(b); --i)
#define FOR1(i,n) FORab(i,1,(n))
#define RFOR1(i,n) RFORab(i,(n),1)
#define FOR(i,n) FORab(i,0,(n)-1)
#define RFOR(i,n) RFORab(i,(n)-1,0)
#define allstl(i,x,t) for (t::iterator i = (x).begin(); i!=(x).end(); ++i)
#define rallstl(i,x,t) for (t::reverse_iterator i = (x).rbegin(); i!=(x).rend(); ++i)
#define begend(x) (x).begin(),(x).end()
#define rbegend(x) (x).rbegin(),(x).rend()
#define ms(a,v) memset(a,v,sizeof(a))
#define msn(a,v,n) memset(a,v,n*sizeof(a[0]))
#define mcp(d,s,n) memcpy(d,s,n*sizeof(s[0]))
#define clamp(x,a,b) min(max(x,a),b)

ll dp[32][2][2][2];

ll sol(int a, int b, int k, bool ax, bool bx, bool kx, int p) {
    if (p == -1) return 1;
    if (dp[p][ax][bx][kx] >= 0) return dp[p][ax][bx][kx];
    ll r = 0;
    // 00
    r += sol(a, b, k, ax or atbit(a,p)==1, bx or atbit(b,p)==1, kx or atbit(k,p)==1, p-1);
    // 10
    if (ax or atbit(a,p)==1) r += sol(a, b, k, ax, bx or atbit(b,p)==1, kx or atbit(k,p)==1, p-1);
    // 01
    if (bx or atbit(b,p)==1) r += sol(a, b, k, ax or atbit(a,p)==1, bx, kx or atbit(k,p)==1, p-1);
    // 11
    if ((kx or atbit(k,p)==1) and (ax or atbit(a,p)==1) and (bx or atbit(b,p)==1)) r += sol(a, b, k, ax, bx, kx, p-1);
    dp[p][ax][bx][kx] = r;
    return r;
}

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.in.out", "wt", stdout);

    int T;
    cin>>T;
    FOR1(cas,T) {
        int a, b, k;
        cin>>a>>b>>k;
        ms(dp, -1);
        ll r = sol(a-1, b-1, k-1, false, false, false, 30);
        printf("Case #%d: %lld\n", cas, r);
    }

    return 0;
}
