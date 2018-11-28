#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
#define rep(i,a,b) for(int i=(a),__tzg_##i=(b);i<__tzg_##i;++i)
#define urp(i,a,b) for(int i=(a),__tzg_##i=(b);i>=__tzg_##i;--i)
#define rp(i,b) rep(i,0,b)
#define repd(i,a,b) rep(i,a,(b)+1)
#define mst(a,b) memset(a,b,sizeof(a))
#define vrp(it,v) for(auto it(v.begin());(it)!=(v.end());++it)
#define vtr(v) (v).begin(),(v).end()
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define pb(a) push_back(a)
#define _0(x) (!(x))
#define _1(x) (x)
#define bit(x,y) (((x)>>(y))&1)
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;

int cal(ll x) {
    int res = 0;
    while (x) {
        res |= 1<<(x%10);
        x /= 10;
    }
    return res;
}

void solve() {
    ll n;
    cin>>n;
    if (!n) {
        puts("INSOMNIA");
        return ;
    }
    int mask = 0, sn = 0;
    rp(i, 10) sn |= 1<<i;
    ll m = n;
    while (1) {
        mask |= cal(m);
        if (mask == sn) {
            cout<<m<<endl;
            return ;
        }
        m += n;
    }
}


int main() {
#ifdef _TZG_DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif // _TZG_DEBUG
    int t;
    cin>>t;
    repd(_, 1, t) {
        printf("Case #%d: ", _);
        solve();
    }
    return 0;
}
