#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int t,k,c,s,i,z;
    scanf("%d",&t);z=1;
    while(t--)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",z);
        for(i=1;i<=k;i++)
            printf("%d ",i);
        printf("\n");
        z++;
    }
    return 0;
}
