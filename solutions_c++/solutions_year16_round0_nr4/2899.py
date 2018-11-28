#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
int t,u,i,s,c,k;
scanf("%d",&t);
for(u=1;u<=t;u++)
{
    scanf("%d %d %d",&k,&c,&s);
    if(k==s)
    {
         printf("Case #%d: ",u);
        for(i=1;i<=k;i++)
        {
           printf("%d ",i);
        }
        printf("\n");
    }
}
    return 0;
}
