#include<bits/stdc++.h>
#define rep(i,s,t) for (ll i=(s); i<=(t); ++i)
#define dep(i,t,s) for (ll i=(t); i>=(s); --i)
#define i first
#define j second
#define pb push_back
#define qb pop_back
#define pf push_front
#define qf pop_front
#define sz(x) ll((x).size())
#define p(i) (1LL<<((i)-1))
#define w(x,i) ((x)&p(i))
#define inf ll(~0u>>1)

using namespace std;

template<class T> inline T pr(T x) { return --x; }
template<class T> inline T nx(T x) { return ++x; }
template<class T> inline T sqr(T x) { return x*x; }

template<class T>
inline void get(T &n) {
    char c = getchar();
    while (c!='-' && (c<'0' || c>'9')) c = getchar();
    n = 0; T s = 1; if (c=='-') s = -1,c = getchar();
    while (c>='0' && c<='9') n*=10,n+=c-'0',c=getchar();
    n *= s;
}

typedef long long ll;
typedef pair<ll,ll> PII;

const ll maxn = 210;
ll n,K;
double f[maxn][maxn],p[maxn];

int main() {
    ll i,j,k,t,tt,Test;
    cin >> Test;
    rep(Ti,1,Test) {
        cin >> n >> K;
        rep(i,1,n) cin >> p[i];
        sort(p+1,p+n+1);
        double ans = 0;
        rep(i,0,K) {
            j = K - i;
            memset(f,0,sizeof(f));
            f[0][0] = 1;
            rep(k,1,K) {
                double pi = k <= i ? p[k] : p[n - (k - i) + 1];
                f[k][0] = (1 - pi) * f[k-1][0];
                rep(l,1,k) {
                    f[k][l] = pi * f[k-1][l-1] + (1 - pi) * f[k-1][l];
                }
            }
            ans = max(ans,f[K][K/2]);
        }
        printf("Case #%lld: %.8f\n",Ti,ans);
    }

    return 0;
}
