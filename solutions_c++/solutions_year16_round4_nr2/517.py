#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
using namespace std;
using namespace __gnu_pbds;
long double ar[205];
vector<long double>ve;
int n,k;
long double dp[205][105];
long double F(){
    dp[0][0]=1;
    for(int i=1;i<=k;i++){
        for(int a=0;a<=(k+1)/2;a++){
            int b=i-a;
            if(b>k/2||a>k/2)continue;
            dp[i][a]=
                ( a ? (dp[i-1][a-1]*ve[i-1]) : 0 )
                +dp[i-1][a]*(1-ve[i-1]);
            //printf("dp [%d] [%d] = %f\n",i,a,dp[i][a]);
            }
        }
    return dp[k][k/2];
    }
int main() {
    int T;
    scanf("%d",&T);
    int t=0;
    while(T--){t++;
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            double tmp;
            scanf("%lf",&tmp);
            ar[i]=tmp;
            }
        sort(ar,ar+n);
        long double ans=0;
        for(int i=0;i<=n;i++){
            ve.clear();
            for(int j=0;j<i;j++)
                ve.push_back(ar[j]);
            for(int j=i+n-k;j<n;j++)
                ve.push_back(ar[j]);
            ans=max(ans,F());
            }
        printf("Case #%d: %.06f\n",t,(double)ans);
        }
    return 0;
    }


//15005 2
//20005 5
//25005 9
//30005 13
//35005 20
//40005 27
//45005 36
