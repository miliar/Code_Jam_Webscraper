#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
int dp[1005][1005]={0};
int main()
{
    int test=1,t,i,j,k;
    scanf("%d",&t);
    for(i=1;i<=1000;i++)
        for(j=1;j<=1000;j++)
            if(j<i)
                dp[i][j]=1000000007;
    dp[1][1]=0;
    dp[2][1]=1;
    dp[3][1]=2;
    dp[3][2]=1;
    for(i=4;i<=1000;i++)
    {
        for(j=1;j<i;j++)
        {
            for(k=0;k<i;k++)
            {
                dp[i][k]=min(dp[i][k],1+dp[j][k]+dp[i-j][k]);
            }
        }
    }
    for(i=1;i<=5 && 0;i++)
    {
        for(j=1;j<=5;j++)
        {
            printf("%d ",dp[i][j]);
        }
        printf("\n");
    }
    while(t--)
    {
        int n,a[1005]={0},ans=1000000007;
        scanf("%d",&n);
        //priority_queue<int,vector<int>,priortise> q;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(i=1;i<=1000;i++)
        {
            int val=i;
            for(j=0;j<n;j++)
            {
                if(i>=a[j])
                    continue;
                else
                    val+=dp[a[j]][i];
            }
            ans=min(ans,val);
        }
        printf("Case #%d: %d\n",test,ans);
        test++;
    }
    return 0;
}
