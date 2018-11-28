#include<bits/stdc++.h>
using namespace std;
int main()
{
int t,d,i,j,ans,tot,need,l;
char s[1001];

freopen("A-small-attempt0.txt","r",stdin);
freopen("Ao.out","w",stdout);
scanf("%d",&t);

for(l=1;l<=t;l++)
{
    scanf("%d",&d);
    scanf(" %s",s);
    tot=(int)s[0]-48;
    ans=0;

    for(i=1;i<=d;i++)
    {
        need=i;
        if(need<=tot)
            tot+=((int)s[i]-48);
        else
        {
            j=need-tot;
            ans+=j;
            tot+=(j+(int)s[i]-48);
        }
    }

    printf("Case #%d: %d\n",l,ans);
}
}
