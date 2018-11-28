#include<bits/stdc++.h>
using namespace std;
int T,k,n;
double p[201];
double dp[201][201];
int main()
{
    cin>>T;
    cout<< setprecision(7);
    for(int data=1;data<=T;data++)
    {
        cin>>n>>k;
        double ans = 0;
        for(int i=1;i<=n;i++)
            cin>>p[i];
        for(int i=0;i<(1<<n);i++)
        {
            int cnt=0;
            for(int j=0;j<n;j++)
                if(i>>j&1)
                    ++cnt;
            if(cnt!=k)continue;
            memset(dp,0,sizeof(dp));
            dp[0][0]=1;
            cnt=0;
            for(int j=0;j<n;j++)
                if(i>>j&1)
                {
                    ++cnt;
                    dp[cnt][0]=dp[cnt-1][0]*(1-p[j+1]);
                    for(int t=1;t<=cnt && t<=k/2;t++)
                        dp[cnt][t]=dp[cnt-1][t-1]*p[j+1]+dp[cnt-1][t]*(1-p[j+1]);
                }
            if(dp[k][k/2]>ans)
                ans=dp[k][k/2];
        }
        cout<<"Case #"<<data<<": ";//<<ans<<endl;
        printf("%.8lf\n",ans);
    }
}
