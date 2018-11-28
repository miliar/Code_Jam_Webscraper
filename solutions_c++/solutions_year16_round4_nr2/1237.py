#include <bits/stdc++.h>

using namespace std;
#define rep(i,a,b) for(int i=(a),__tzg_##i=(b);i<__tzg_##i;++i)
#define urp(i,a,b) for(int i=(a),__tzg_##i=(b);i>=__tzg_##i;--i)
#define rp(i,b) rep(i,0,b)
#define repd(i,a,b) rep(i,a,(b)+1)
#define mst(a,b) memset(a,b,sizeof(a))
#define vtr(v) (v).begin(),(v).end()
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define pb(a) push_back(a)
#define _0(x) (!(x))
#define _1(x) (x)
#define bit(x,y) (((x)>>(y))&1)
#define siz(x) ((int)(x).size())
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;

const int N = 20;
double p[N];
inline int cal(int x) {
    int r = 0;
    while (x) {
        ++r;
        x &= x-1;
    }
    return r;
}
double q[N];
void solve() {
    int n, k;
    cin>>n>>k;
    rp(i, n) cin>>p[i];
    set<int> mmp;
    double res = 0.0;
    rp(mask, 1<<n) {
        int cnt = cal(mask);
        if (cnt != k) continue;
        int m = 0;
        int o = 0;
        rp(i, n) if (bit(mask, i)) m |= 1<<i;
        if (mmp.count(m))
            continue;
        mmp.insert(m);
        rp(i, n) if (bit(mask, i)) q[o++] = p[i];
        double tr = 0.0;
        rp(f, 1<<k) {
            int u = cal(f);
            if (u != k/2) continue;
            double y = 1.0;
            rp(i, k) {
                if (bit(f, i)) {
                    y *= q[i];
                } else {
                    y *= 1.0-q[i];
                }
            }
            tr += y;
        }
        if (tr > res) res = tr;
    }
    printf("%.7lf\n", res);
}

int main() {
#ifdef _TZG_DEBUG
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out_b.txt", "w", stdout);
#endif // _TZG_DEBUG
    int t;
    cin>>t;
    repd(_,1,t) {
        printf("Case #%d: ", _);
        solve();
    }
    return 0;
}
