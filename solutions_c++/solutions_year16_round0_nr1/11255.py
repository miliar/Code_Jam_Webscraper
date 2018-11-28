#include <bits/stdc++.h>
//#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;

#define ll long long
#define SZ(x) ((int)(x).size()) 
#define ALL(v) (v).begin(), (v).end()
#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)
#define reveach(i, v) for (__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++ i) 
#define REP(i,a,n) for ( int i=a; i<int(n); i++ )
#define FOR(i,a,n) for ( int i=n-1; i>= int(a);i-- )
#define lson rt<<1, L, m
#define rson rt<<1|1, m, R
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define fi first
#define se second
#define CLR(a, b) memset(a, b, sizeof(a))
#define Min(a, b) a = min(a, b)
#define Max(a, b) a = max(a, b)
const int maxn = 1e6 + 7;
int T;
int kase;
int n;
int vis[13];

ll solve(ll x){
    if(x == 0) return -1;
    CLR(vis, 0);
    int i = 1;
    for(i = 1; ; i++){
        ll t = x * i;
        while(t){
            vis[t%10] = 1;
            t /= 10;
        }
        int ok = 1;
        REP(j, 0, 10) if(!vis[j]) ok = 0;
        if(ok) break;
    }
    return i * x;
}
int main(){
#ifdef ac
    freopen("in.txt","r",stdin);
#endif
    freopen("out.txt","w",stdout);
    scanf("%d", &T);
    while(T--){
        scanf("%d", &n);
        printf("Case #%d: ", ++kase);
        ll res = solve(n);
        if(res == -1) puts("INSOMNIA");
        else printf("%lld\n", res);
    }
    /*
    REP(i, 1, 2){
        printf("%lld, ", solve(i));
    }
    */
    return 0;
}
