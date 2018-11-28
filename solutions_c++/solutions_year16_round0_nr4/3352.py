#include<stdio.h>
int main()
{
     freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        int k,c,s;
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",i+1);
        for(j=1;j<=k;j++)
            printf("%d ",j);

            printf("\n");
    }
    return 0;
}
