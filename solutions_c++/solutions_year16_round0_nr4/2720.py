#include<cstdio>
#include<stdlib.h>
main()
{
    freopen("def.txt","w",stdout);
    int t;
    int h;
    int x,y;
    int i,j;
    int k,c,s;
    scanf("%d",&t);
    for(h=1;h<=t;h++)
    {
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d: ",h);
        if(k==1)
        {
            printf("1\n");
        }
        else if(k==2)
        {
            if(c==1&&s==1)
            {
                printf("IMPOSSIBLE\n");
            }
            else if(c==1)
            {
                printf("1 2\n");
            }
            else
            {
                printf("2\n");
            }
        }
        else if(s==1)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            for(i=1;i<=k;i++)
            {
                printf("%d ",i);
            }
            printf("\n");
        }
    }
}
