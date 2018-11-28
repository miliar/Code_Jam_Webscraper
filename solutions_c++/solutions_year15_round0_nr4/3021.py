#include<stdio.h>
int main ()
{
    int i,x,r,c,t;

    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d",&t);
    for(i = 1; i <= t; i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(x == 1)
        {
            printf("Case #%d: GABRIEL\n",i);
            continue;
        }
        if(x == 2)
        {
            if(r * c % 2 == 0)
                printf("Case #%d: GABRIEL\n",i);
            else
                printf("Case #%d: RICHARD\n",i);
            continue;
        }
        if(x == 3)
        {
            if(r * c % 3 != 0)
            {
                printf("Case #%d: RICHARD\n",i);
                continue;
            }
            if(r + c >= 5)
            {
                printf("Case #%d: GABRIEL\n",i);
                continue;
            }
            printf("Case #%d: RICHARD\n",i);
            continue;
        }
        if(r * c % 4 != 0)
        {
            printf("Case #%d: RICHARD\n",i);
            continue;
        }
        if(r == 1 || c == 1 || r == 2 || c == 2)
        {
            printf("Case #%d: RICHARD\n",i);
            continue;
        }
        printf("Case #%d: GABRIEL\n",i);
        continue;
    }

    return 0;
}
