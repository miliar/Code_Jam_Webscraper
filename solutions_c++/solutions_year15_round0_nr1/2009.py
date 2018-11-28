#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 2010;

char s [MXN];

int solve(){
    int t;
    scanf("%d %s", &t, s);
    int cur = 0;
    int res = 0;
    rep(i,t+1){
        int k = s[i]-'0';
        if(!k) continue;
        if( i>cur ){
            int d = i-cur;
            res+=d;
            cur+=d;
        }
        cur+=k;
    }
    return res;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    rep(i,T) printf("Case #%d: %d\n", i+1, solve());
    return 0;
}
