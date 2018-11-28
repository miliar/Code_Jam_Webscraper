#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int i,t,tc,x,r,c;
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        scanf("%d",&x);
        scanf("%d",&r);
        scanf("%d",&c);
        if(x==1)
        {
            printf("Case #%d: GABRIEL\n",t);
            continue;
        }
        else if(x==2)
        {
            if(((r*c)%2)==1)
            {
                printf("Case #%d: RICHARD\n",t);
            }
            else
            {
                printf("Case #%d: GABRIEL\n",t);
            }
        }
        else if(x==3)
        {
            if((r==1)||(c==1))
            {
                printf("Case #%d: RICHARD\n",t);
            }
            else if(((r*c)%3)==0)
            {
                printf("Case #%d: GABRIEL\n",t);
            }
            else
            {
                printf("Case #%d: RICHARD\n",t);
            }
        }
        else if(x==4)
        {
            if(((r*c)<10))
            {
                printf("Case #%d: RICHARD\n",t);
            }
            else
            {
                printf("Case #%d: GABRIEL\n",t);
            }
        }
    }
    return 0;
}

