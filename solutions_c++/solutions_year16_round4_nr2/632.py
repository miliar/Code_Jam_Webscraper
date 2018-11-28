#include<bits/stdc++.h>
using namespace std;
double dp1[300][300],dp2[300][300];
main(){
    //freopen("B-small-attempt2.in","r",stdin);
    //freopen("pb.txt","w",stdout);
    int T,n,k,cas=1;
    double ary[300];
    scanf("%d",&T);
    while(T--){
        int i,j;
        memset(ary,0,sizeof(ary));
        scanf("%d%d",&n,&k);
        for(i=1;i<=n;i++)scanf("%lf",&ary[i]);
        sort(ary,ary+n);
        memset(dp1,0,sizeof(dp1));
        memset(dp2,0,sizeof(dp2));
        dp1[1][1]=ary[1],dp1[1][0]=1-ary[1];
        for(i=2;i<=n;i++){
            dp1[i][0]=dp1[i-1][0]*(1-ary[i]);
            for(j=1;j<=i;j++)dp1[i][j]=dp1[i-1][j]*(1-ary[i])+dp1[i-1][j-1]*ary[i];
        }
        dp2[n][1]=ary[n],dp2[n][0]=1-ary[n];
        for(i=n-1;i>=1;i--){
            dp2[i][0]=dp2[i+1][0]*(1-ary[i]);
            for(j=1;j<=n-i+1;j++)dp2[i][j]=dp2[i+1][j]*(1-ary[i])+dp2[i+1][j-1]*ary[i];
        }
        int d=n-k;
        double p,ans=0;
        for(i=1;i<=n;i++,puts(""))for(j=0;j<=i;j++)printf("%f ",dp1[i][j]);
        for(i=1;i<=n;i++,puts(""))for(j=0;j<=n-i+1;j++)printf("%f ",dp2[i][j]);
        for(i=2;i+d-1<n;i++){
            p=0;
            for(j=0;j<=min(k/2,i);j++)p+=dp1[i-1][j]*dp2[i+d][k/2-j];
            ans=max(ans,p);
        }
        ans=max(max(dp1[k][k/2],dp2[n-k+1][k/2]),ans);
        printf("Case #%d: %.7f\n",cas++,ans);
    }
}
