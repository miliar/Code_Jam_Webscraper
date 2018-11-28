#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int dp[15];
char s[15];
int main()
{
    int T,n;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int k=0;
    scanf("%d",&T);
    while(T--)
    {
        memset(dp,0,sizeof(dp));
        scanf("%d",&n);
        scanf("%s",s);
        int ans1=s[0]-'0';
        int ans=0;
        for(int i=1;i<=n;i++)
        {
            if(ans1>=i)
            {
                ans1+=s[i]-'0';
                continue;
            }
            else
            {
               ans+=i-ans1;
               ans1+=(i-ans1)+s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",++k,ans);
    }
    return 0;
}
