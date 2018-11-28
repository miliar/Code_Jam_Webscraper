#include<stdio.h>
#include<string.h>
int main()
{
    int t;
    int x,r,c,cases;
    while(scanf("%d",&t)!=EOF)
    {
        cases=0;
        while(t--)
        {
            cases++;
            scanf("%d%d%d",&x,&r,&c);
            if(x==1)
            {
                printf("Case #%d: GABRIEL\n",cases);
                continue;
            }
            else if(x==2)
            {
                if((r*c)%2==0)
                {
                    printf("Case #%d: GABRIEL\n",cases);
                    continue;
                }
                else
                {
                    printf("Case #%d: RICHARD\n",cases);
                    continue;
                }
            }
            else if(x==3)
            {
                if(r*c==6||r*c==9||r*c==12)
                {
                    printf("Case #%d: GABRIEL\n",cases);
                    continue;
                }
                else
                {
                    printf("Case #%d: RICHARD\n",cases);
                    continue;
                }
            }
            else if(x==4)
            {
                if(r*c==12||r*c==16)
                {
                    printf("Case #%d: GABRIEL\n",cases);
                    continue;
                }
                else
                {
                    printf("Case #%d: RICHARD\n",cases);
                    continue;
                }
            }
        }
    }
    return 0;
}
