#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
double a[205];
double dp1[205][205];
double dp2[205][205];
int main()
{
    freopen("B-large (2).in","r",stdin);
    freopen("b2.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1; i<=n; ++i)
            scanf("%lf",a+i);
        sort(a+1,a+n+1);
        memset(dp1,0,sizeof(dp1));
        memset(dp2,0,sizeof(dp2));
        dp1[0][0]=dp2[n+1][0]=1;
        for(int i=1; i<=n; ++i)
            for(int j=0; j<=i; ++j)
            {
                dp1[i][j]=dp1[i-1][j]*(1-a[i]);
                if(j>0)
                    dp1[i][j]+=dp1[i-1][j-1]*a[i];
            }
        for(int i=n; i>=0; --i)
            for(int j=0; j<=n+1-i; ++j)
            {
                dp2[i][j]=dp2[i+1][j]*(1-a[i]);
                if(j>0)
                    dp2[i][j]+=dp2[i+1][j-1]*a[i];
            }

//        for(int i=0;i<=n;++i)
//            for(int j=0;j<=n;++j)
//                printf("%f%c",dp1[i][j]," \n"[j==n]);
//        puts("---------");
//        for(int i=0;i<=n;++i)
//            for(int j=0;j<=n;++j)
//                printf("%f%c",dp2[i][j]," \n"[j==n]);
        double ans=0;
        for(int i=0; i<=k; ++i)
        {
            double temp=0;
            for(int j=0;j<=k/2;++j)
                temp+=dp1[i][j]*dp2[n-(k-i)+1][(k/2-j)];
            ans=max(ans,temp);
        }
        printf("Case #%d: %.10f\n",++ca,ans);
    }
}
