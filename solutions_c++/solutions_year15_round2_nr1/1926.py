#include<bits/stdc++.h>
using namespace std;
#define ll long long

int dp[1000005];

int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,T,n,ans,tmp,pal,cnt;
    for(i=1;i<=20;i++)  dp[i]=i;
    for(i=21;i<1000005;i++)
    {
        dp[i]=dp[i-1]+1;
        if((i%10)==0)
            continue;
        tmp=i;pal=0;cnt=0;
        while(tmp)
        {
            pal=pal*10+tmp%10;
            tmp=tmp/10;
            cnt++;
        }
        if(pal<i)
        {
            dp[i]=min(dp[i],dp[pal]+1);
        }
    }
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",t);
        printf("%d\n",dp[n]);
    }
    return 0;
}



