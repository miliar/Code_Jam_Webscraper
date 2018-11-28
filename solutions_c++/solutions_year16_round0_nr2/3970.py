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

char s[200];
void solve() {
    cin>>s;
    int l = 0, r = strlen(s)-1;
    int ed = r+1;
    urp(i, r, l) {
        if (s[i] != '+') {
            ed = i;
            break;
        }
    }
    if (ed == r+1) {
        printf("%d\n", 0);
        return;
    }
    int cnt = 0;
    char pre = '+';
    urp(i, ed, 0) {
        if (pre != s[i]) ++cnt;
        pre = s[i];
    }
    printf("%d\n", cnt);
}


int main() {
#ifdef _TZG_DEBUG
    freopen("B-large.in", "r", stdin);
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
