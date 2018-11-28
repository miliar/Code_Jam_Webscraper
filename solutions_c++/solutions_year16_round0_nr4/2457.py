#include <cstdio>
int nrt,i,j,k,c,s;
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    scanf("%d",&nrt);
    for(i=1;i<=nrt;i++)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",i);
        for(j=1;j<=s;j++)
            printf("%d ",j);
        printf("\n");
    }
    return 0;
}
