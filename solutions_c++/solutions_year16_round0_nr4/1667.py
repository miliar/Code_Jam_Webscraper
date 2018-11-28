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

const ll maxn = 110;
ll K,c,s,p[maxn];

int main() {
    ll i,j,k,t,tt,Test;
    get(Test);
    rep(Ti,1,Test) {
        printf("Case #%lld:",Ti);
        get(K); get(c); get(s);
        p[0] = 1;
        rep(i,1,c) p[i] = p[i-1] * K;
        rep(i,1,c) p[i] += p[i-1];
        rep(i,1,K) printf(" %lld",(i-1) * p[c-1] + 1);
        puts("");
    }

    return 0;
}
