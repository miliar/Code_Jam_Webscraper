#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,x,r,c;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
        {
            printf("Case #%d: GABRIEL\n",i);
        }
        else if(x==2)
        {
            if((r*c)%2==0)
                printf("Case #%d: GABRIEL\n",i);
            else
                printf("Case #%d: RICHARD\n",i);
        }
        else if(x==3)
        {
            if(r==1||c==1)
                printf("Case #%d: RICHARD\n",i);
            else if(r==3||c==3)
                printf("Case #%d: GABRIEL\n",i);
            else
                printf("Case #%d: RICHARD\n",i);
        }
        else if(x==4)
        {
            if(r==4&&c==4)
                printf("Case #%d: GABRIEL\n",i);
            else if(r==3&&c==4)
                printf("Case #%d: GABRIEL\n",i);
            else if(r==4&&c==3)
                printf("Case #%d: GABRIEL\n",i);
            else
                printf("Case #%d: RICHARD\n",i);
        }
    }
return 0;
}

