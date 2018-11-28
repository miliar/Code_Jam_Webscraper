#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("C1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d: ",i);
        for(int j=1;j<=k;j++)
            printf("%d ",j);
            printf("\n");
    }
    return 0;
}
