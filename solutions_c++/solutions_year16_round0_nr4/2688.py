#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("fractilesmall_output.txt","w",stdout);
    int t,k,c,s,nub=1,i;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",nub++);
        for(i=1;i<=k;i++)
            printf("%d ",i);
        printf("\n");
    }
}
