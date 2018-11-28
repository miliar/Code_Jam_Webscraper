#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,j,counti,ans,n,i;
    char s[2000];
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        counti=0,ans=0;
        scanf("%d %s",&n,s);
        for(i=0;i<=n;i++)
        {
            if(counti<i)
            {
                ans+=i-counti;
                counti=i;
            }
            counti+=s[i]-'0';
        }
        printf("Case #%d: %d\n",j,ans);
    }
}
