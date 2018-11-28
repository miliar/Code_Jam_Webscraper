#include<bits/stdc++.h>

using namespace std;
int t,i,j,k,l,ans,s,total;
char c[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d %s",&s,c);
        total=ans=0;
        for(i=0;i<=s;i++)
        {
            if(total<i)
            {
                ans+=(i-total);
                total+=(i-total);
            }
            total+=(c[i]-'0');
        }
        printf("Case #%d: %d\n",l,ans);
    }
    return 0;
}
