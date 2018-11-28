#include<stdio.h>
int main()
{
    freopen("last.in", "rt", stdin);
    freopen("answer1.txt", "wt", stdout);
    int t,x,r,c,temp,p;
    scanf("%d",&t);
    p=t;
    while(t--)
    {
        scanf("%d %d %d",&x,&r,&c);
        if(r<c)
        {
            temp=r;
            r=c;
            c=temp;
        }
        if(x==4)
        {
            if(r==4)
            {
                if(c==4)
                {
                    printf("Case #%d: GABRIEL\n",p-t);
                }
                else if(c==3)
                {
                    printf("Case #%d: GABRIEL\n",p-t);
                }
                else
                    printf("Case #%d: RICHARD\n",p-t);
            }
            else
                printf("Case #%d: RICHARD\n",p-t);
        }
        if(x==3)
        {
            if(r==4)
            {
                if(c==3)
                {
                    printf("Case #%d: GABRIEL\n",p-t);
                }
                else
                    printf("Case #%d: RICHARD\n",p-t);
            }
            else if(r==3)
                {
                    if(c==3)
                    {
                        printf("Case #%d: GABRIEL\n",p-t);
                    }
                    else if(c==2)
                    {
                        printf("Case #%d: GABRIEL\n",p-t);
                    }
                    else
                        printf("Case #%d: RICHARD\n",p-t);
                }
            else
                printf("Case #%d: RICHARD\n",p-t);
        }
        if(x==2)
        {
            if(r==4)
            {
                    printf("Case #%d: GABRIEL\n",p-t);
            }
            else if(r==3)
            {
                if(c==2)
                    printf("Case #%d: GABRIEL\n",p-t);
                else
                     printf("Case #%d: RICHARD\n",p-t);
            }
            else if(r==2)
            {
                printf("Case #%d: GABRIEL\n",p-t);
            }
            else
                printf("Case #%d: RICHARD\n",p-t);
        }
        if(x==1)
        {
            printf("Case #%d: GABRIEL\n",p-t);
        }

    }
    return 0;
}
