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
const int inf = 1e9;

char s [MXN];

int a [MXN];
int dp [MXN];

int solve(){
    int n;
    scanf("%d", &n);
    int mx = 0;
    rep(i,n) scanf("%d", &a[i]);
    rep(i,n) mx = max(mx,a[i]);

    int res = inf;

    forn(i,1,mx+1){
        rep(j,mx+1){
            if(j<=i) dp[j] = 0;
            else dp[j] = min( dp[j-i]+1, dp[j/2] + dp[(j+1)/2] + 1 );
        }
        int sum = i;
        rep(j,n){
            sum += dp[ a[j] ];
        }
        if( sum < res ) res = sum;
    }

    return res;
}

int main()
{
    freopen("in.txt", "r", stdin);    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);



    rep(i,T){
        int q = solve();
        printf("Case #%d: %d\n", i+1, q);
    }
    return 0;
}
