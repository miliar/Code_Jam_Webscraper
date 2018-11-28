#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cas,n,sum,ans,i;
    char s[1005];
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        sum=0,ans=0;
        scanf("%d %s",&n,s);
        for(i=0;i<=n;i++)
        {
            if(sum<i)ans+=i-sum,sum=i;
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
