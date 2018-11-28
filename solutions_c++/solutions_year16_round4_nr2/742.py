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

const int MXN = 210;

double p [MXN];
double dp [MXN][MXN];

int n,k;

double bst;

double pp [MXN];

void dfs(int ii, int tk){
    if(ii==n){
        if(tk != k){
            return ;
        }
        rep(i, k + 1){
            rep(j, k/2 + 1){
                dp[i][j] = 0;
            }
        }
        dp[0][0] = 1;
        rep(i, k){
            rep(j, k/2 + 1){
                dp[i+1][j] += dp[i][j] * (1 - pp[i]);
                dp[i+1][j+1] += dp[i][j] * pp[i];
            }
        }
        bst = max(bst, dp[k][k/2]);
        return ;
    }
    if(tk==k){
        dfs(ii+1, tk);
        return;
    }
    pp[tk] = p[ii];
    dfs(ii+1, tk+1);
    dfs(ii+1, tk);
}

double solve(){
    scanf("%d%d", &n, &k);
    rep(i,n) scanf("%lf", &p[i]);
    
    bst = 0;
    dfs(0, 0);
    
    return bst;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
    

    int T;
    scanf("%d", &T);
    //cout << "kek";
    rep(i,T){
        printf("Case #%d: %.9f\n", i+1, solve());
    }

    return 0;
}
