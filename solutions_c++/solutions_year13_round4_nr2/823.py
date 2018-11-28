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
typedef float flt;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define eps 1e-9
#define inf 1000000000
#define infll 1000000000000000000LL
#define abs(x) ((x)<0?-(x):(x))
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
#define ms(a,v) memset(a,v,sizeof(a))
#define msn(a,v,n) memset(a,v,n*sizeof(a[0]))
#define mcp(d,s,n) memcpy(d,s,n*sizeof(s[0]))
#define clamp(x,a,b) min(max(x,a),b)

bool mustprize(int i, int n, ll p) {
    ll up = i, down = n-i-1;
    ll lopos = 0;
    FOR(g,n) {
        lopos <<= 1;
        if (up) {
            --up; // one beats i
            up /= 2; // rest get same recs
            lopos |= 1;
        }
    }
    return lopos < p;
}

bool canprize(int i, int n, ll p) {
    ll up = i, down = (1LL<<n)-i-1;
    ll hipos = 0;
    FOR(g,n) {
        hipos <<= 1;
        if (down) {
            --down; // beaten
            down /= 2; // rest get same recs
        } else {
            hipos |= 1;
        }
    }
    return hipos < p;
}

int main() {
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("B-small-attempt0.in.out", "wt", stdout);

    int T;
    cin>>T;
    FOR1(cas,T) {
        int n;
        ll p;
        cin>>n>>p;
        ll mpx = 0, cpx = 0;
        {
            ll hi = (1LL<<n)-1, lo = 0;
            while (lo < hi) {
                int mid = (hi + lo + 1) / 2;
                if (mustprize(mid, n, p)) {
                    lo = mid;
                } else {
                    hi = mid - 1;
                }
            }
            mpx = lo;
        }
        {
            ll hi = (1LL<<n)-1, lo = 0;
            while (lo < hi) {
                int mid = (hi + lo + 1) / 2;
                if (canprize(mid, n, p)) {
                    lo = mid;
                } else {
                    hi = mid - 1;
                }
            }
            cpx = lo;
        }
        cout<<"Case #"<<cas<<": "<<mpx<<" "<<cpx<<endl;
    }

    return 0;
}
