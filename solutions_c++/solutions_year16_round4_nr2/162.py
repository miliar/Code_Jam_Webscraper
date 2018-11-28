#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn=207;

double q[maxn],p[maxn],dp[maxn][maxn],res;
int T,n,k;

int main(){
//    freopen("input.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        printf("Case #%d: ",tt);
        scanf("%d%d",&n,&k);
        for(int i=1; i<=n; ++i) scanf("%lf",&q[i]);
        sort(q+1,q+n+1);
        double res=0;
        for(int i=0; i<=k; ++i){
            int c=0;
            for(int j=1; j<=i; ++j){
                p[++c]=q[j];
            }
            for(int j=n; j>=1 && c<k; --j){
                p[++c]=q[j];
            }
            sort(p+1,p+c+1);
            reset(dp,0);
            dp[0][0]=1;
            for(int i=1; i<=k; ++i) for(int v=0; v<=min(i,k/2); ++v){
                if(v>0) dp[i][v]+=dp[i-1][v-1]*p[i];
                dp[i][v]+=dp[i-1][v]*(1-p[i]);
            }
            res=max(res,dp[k][k/2]);
        }

        printf("%0.9f\n",res);

    }
}

