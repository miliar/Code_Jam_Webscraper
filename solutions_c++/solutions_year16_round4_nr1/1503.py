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

int mmp[3][3];
#define P 0
#define R 1
#define S 2
void init() {
    mmp[R][P] = -1;
    mmp[R][R] = 0;
    mmp[R][S] = 1;
    mmp[P][P] = 0;
    mmp[P][R] = 1;
    mmp[P][S] = -1;
    mmp[S][P] = 1;
    mmp[S][S] = 0;
    mmp[S][R] = -1;
}
const int N = 10;
int num[N], tp[N];
int tol, n;
int go() {
    rp(i, tol) tp[i] = num[i];
    rp(i, n) {
        int all = 1<<(n-i);
        int o = 0, q;
        for (int j = 0; j < all; j += 2) {
            q = mmp[tp[j]][tp[j+1]];
            if (q == 0) return 0;
            if (q > 0) tp[o++] = tp[j];
            else tp[o++] = tp[j+1];
        }
    }
    return 1;
}
void solve() {
    int r, p, s;
    cin>>n>>r>>p>>s;
    tol = 1<<n;
    int c = 0;
    rp(i, r) num[c++] = R;
    rp(i, p) num[c++] = P;
    rp(i, s) num[c++] = S;
    sort(num, num+tol);
    do{
        if (go()) {
            rp(i, tol) {
                switch(num[i]) {
                case R: printf("R"); break;
                case P: printf("P"); break;
                case S: printf("S"); break;
                }
            }
            puts("");
            return ;
        }
    }while (next_permutation(num, num+tol));
    puts("IMPOSSIBLE");
}

int main() {
#ifdef _TZG_DEBUG
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out_a.txt", "w", stdout);
#endif // _TZG_DEBUG
    int t;
    cin>>t;
    init();
    repd(_,1,t) {
        printf("Case #%d: ", _);
        solve();
    }
    return 0;
}
