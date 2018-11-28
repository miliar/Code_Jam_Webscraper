#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>

using namespace std;

int main()
{
    int t;
    scanf("%i",&t);
    for(int i=1;i<=t;i++)
    {
        int x,r,c;
        scanf("%i%i%i",&x,&r,&c);
        int brick=r*c;
        if(x==1)
        {
            printf("Case #%i: GABRIEL\n",i);
        }
        else if(x==2)
        {
            if(brick%2==0)
            {
                printf("Case #%i: GABRIEL\n",i);
            }
            else
            {
                printf("Case #%i: RICHARD\n",i);
            }
        }
        else if(x==3)
        {
            if(brick==3)
            {
                printf("Case #%i: RICHARD\n",i);
            }
            else if(brick%3==0)
            {
                printf("Case #%i: GABRIEL\n",i);
            }
            else
            {
                printf("Case #%i: RICHARD\n",i);
            }
        }
        else if(x==4)
        {
            if(brick<=4 || brick%4!=0)
            {
                printf("Case #%i: RICHARD\n",i);
            }
            else if(r==4 && c==4)
            {
                printf("Case #%i: GABRIEL\n",i);
            }
            else if(r==4 && c==3)
            {
                printf("Case #%i: GABRIEL\n",i);
            }
            else if(r==3 && c==4)
            {
                printf("Case #%i: GABRIEL\n",i);
            }
            else
            {
                printf("Case #%i: RICHARD\n",i);
            }
        }
    }
}
