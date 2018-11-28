#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define sqr(x) ((x)*(x))
#define mem(a,x) memset(a,x,sizeof(a))
#define REP(i,n) for (int i=0; i<(n); i++)
#define rep(i,n) for (int i=1; i<=(n); i++)
#define For(i,s,t) for (int i=(s); i<=(t); i++)
#define FOR(i,s,t) for (int i=(s); i>=(t); i--)
#define foreach(j,x) for (int j=adj[x]; j>=0; j=E[j].nxt)
#define Foreach(it,v) for (__typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)
typedef long long lld;
typedef pair<int,int> pii;
typedef set<int>::iterator setIter;

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int cas; scanf("%d",&cas);
    rep(cs,cas) {
        int n,m,selc[50];
        double a[50];
        scanf("%d%d",&n,&m);
        rep(i,n) scanf("%lf",&a[i]);
        mem(selc,0);
        For(i,n-m+1,n) selc[i]=1;
        double ans=0;
        do {
            vector<double> b;
            rep(i,n) if (selc[i]) b.pb(a[i]);
            double dp[50][50]; mem(dp,0);
            dp[0][m+1] = b[0];
            dp[0][m-1] = 1-b[0];
            For(i,0,m-2) For(j,0,2*m) if (dp[i][j]) {
                dp[i+1][j+1] += dp[i][j]*b[i+1];
                dp[i+1][j-1] += dp[i][j]*(1-b[i+1]);
            }
            ans=max(ans,dp[m-1][m]);
            //REP(i,m) printf("%.2lf ",b[i]); printf("\n");
        } while (next_permutation(selc+1,selc+n+1));
        printf("Case #%d: %.9lf\n",cs,ans);
    }
    return 0;
}
