#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
int dp[1005][1005]={0};
int main()
{
    int test=1,t;
    scanf("%d",&t);
    while(t--)
    {
        int ans=0,n,i,sum=0;
        char s[1005];
        scanf("%d",&n);
        scanf("%s",s);
        for(i=0;i<=n;i++)
        {
            if(i>sum && s[i]!='0')
            {
                ans+=(i-sum);
                sum=i;
            }
            else
            {
                ;
            }
            sum+=(s[i]-'0');
            //printf("i=%d sum=%d ans=%d\n",i,sum,ans);
        }
        printf("Case #%d: %d\n",test,ans);
        test++;
    }
    return 0;
}
