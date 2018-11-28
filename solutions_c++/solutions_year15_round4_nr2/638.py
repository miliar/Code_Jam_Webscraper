#include<bits/stdc++.h>
#define rep(i,s,t) for (i=(s); i<=(t); ++i)
#define dep(i,t,s) for (i=(t); i>=(s); --i)
#define sz(x) ll((x).size())
#define p(i) (1LL<<((i)-1))
#define w(x,i) ((x)&p(i))
#define fi first
#define se second
#define dll "%lld"

using namespace std;

typedef int ll;
typedef unsigned long long ull;
typedef pair<ll,ll> PII;

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

ll T,Test;
const ll maxn = 110;
ll n;
long double v,x,ans;
#define eps 1e-12

struct Point{
    long double r,c;
}s[maxn];

bool cmp(Point a,Point b) {
    return a.c < b.c;
}

inline void put(long double x) {
    printf("%.8Lf\n",x);
}

int main() {
    ll i,j,k,t,tt;
    get(Test);
    rep(T,1,Test) {
        get(n);
        scanf("%Lf%Lf",&v,&x);
        rep(i,1,n) scanf("%Lf%Lf",&s[i].r,&s[i].c);
        printf("Case #%d: ",T);
        sort(s+1,s+n+1,cmp);
        long double sr = 0,ss = 0;
        rep(i,1,n) {
            sr += s[i].r;
            ss += (s[i].c-x)*s[i].r;
        }
        if (-eps<ss && ss<eps) put(v/sr);
        else if (ss<-eps) {
            rep(i,1,n) {
                long double css = (s[i].c-x)*s[i].r;
                if (ss-css<-eps) sr -= s[i].r,ss -= css;
                else { sr -= ss/(s[i].c-x); ss = 0; break; }
            }
            if (sr<eps) puts("IMPOSSIBLE");
            else put(v/sr);
        }
        else if (ss>eps) {
            dep(i,n,1) {
                long double css = (s[i].c-x)*s[i].r;
                if (ss-css>eps) sr -= s[i].r,ss -= css;
                else {  sr -= ss/(s[i].c-x); ss = 0; break; }
            }
            if (sr<eps) puts("IMPOSSIBLE");
            else put(v/sr);
        }
    }

    return 0;
}
