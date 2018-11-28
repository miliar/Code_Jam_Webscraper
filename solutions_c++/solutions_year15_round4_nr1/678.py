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
ll n,m,cost[maxn][maxn],ans;
char a[maxn][maxn];

int main() {
    ll i,j,k,t,tt; bool flag;
    get(Test);
    rep(T,1,Test) {
        get(n); get(m);
        rep(i,1,n) {
            scanf("%s",a[i]+1);
            rep(j,1,m) cost[i][j] = (a[i][j]!='.' ? 2 : 0);
        }
        rep(i,1,n) {
            flag = false;
            rep(j,1,m) if (a[i][j]!='.') {
                if (flag) cost[i][j] = min(cost[i][j],a[i][j]=='<'?0:1);
                flag = true;
            }
        }
        rep(i,1,n) {
            flag = false;
            dep(j,m,1) if (a[i][j]!='.') {
                if (flag) cost[i][j] = min(cost[i][j],a[i][j]=='>'?0:1);
                flag = true;
            }
        }
        rep(j,1,m) {
            flag = false;
            rep(i,1,n) if (a[i][j]!='.') {
                if (flag) cost[i][j] = min(cost[i][j],a[i][j]=='^'?0:1);
                flag = true;
            }
        }
        rep(j,1,m) {
            flag = false;
            dep(i,n,1) if (a[i][j]!='.') {
                if (flag) cost[i][j] = min(cost[i][j],a[i][j]=='v'?0:1);
                flag = true;
            }
        }
        ans = 0;
        rep(i,1,n)
            rep(j,1,m) {
                if (cost[i][j]==2) ans = -1;
                if (ans>=0) ans += cost[i][j];
            }
        printf("Case #%d: ",T);
        if (ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }

    return 0;
}
