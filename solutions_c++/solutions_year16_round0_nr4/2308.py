#include<stdio.h>
main()
{
    int tt;
    scanf("%d",&tt);
    for(int ttt=0;ttt<tt;ttt++)
    {
        int k,n,m;
        scanf("%d %d %d",&k,&n,&m);
        printf("Case #%d: ",ttt+1);
        for(int i=1;i<=k;i++)
            printf("%d ",i);
        printf("\n");
    }
}
