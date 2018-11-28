#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define min(a,b) ( a < b ? a : b )
#define max(a,b) ( a > b ? a : b )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

vector<int> in;

int solv(int now) {
    int ret(0), i;
    rep(i, in.size()) { ret += in[i] / now - (in[i] % now == 0); }
    return ret;
}

int main() {
    int i, n, p, t, tt, maxn, ans;
    cin >> tt;
    xrep(t, 1, tt+1) {
        cin >> n;
        in.clear();
        maxn = 0;
        rep(i, n) {
            cin >> p;
            maxn = max(maxn, p);
            in.push_back(p);
        }
        ans = maxn;
        xrep(i, 1, maxn) { ans = min(ans, solv(i)+i); }
        
        cout << "Case #" << t << ": " << ans << endl;
    }
}
