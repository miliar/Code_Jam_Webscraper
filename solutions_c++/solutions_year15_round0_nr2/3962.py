#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int num[10];
int dp[10][60];
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    int c=t;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        memset(dp,0x3f,sizeof(dp));
        dp[0][0]=0;
        int sum=0;
        for(int i=1;i<=n;i++)
            scanf("%d",&num[i]);
        for(int i=1;i<=n;i++)
        {
            for(int j=0;j<num[i];j++)
            {
                for(int w=0;w<=sum;w++)
                {
                    dp[i][w+j]=min(dp[i][j+w],w+j+max(dp[i-1][w]-w,num[i]/(j+1)+(num[i]%(j+1)!=0)));
                }
            }
            sum+=num[i]-1;
//            for(int j=0;j<=sum;j++)
//                cout<<dp[i][j]<<ends;
//            cout<<endl;
        }
        int ans=dp[n][0];
        for(int i=0;i<=sum;i++)
            ans=min(ans,dp[n][i]);
        printf("Case #%d: %d\n",c-t,ans);
    }
    return 0;
}
