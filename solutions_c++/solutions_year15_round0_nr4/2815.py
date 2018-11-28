#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{
    freopen("inputb.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int j=1; j<=t; j++)
    {
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);
        if(x==1)
            printf("Case #%d: GABRIEL\n",j);
        else if(x==2)
        {
            if(r*c%x==0)
                printf("Case #%d: GABRIEL\n",j);
            else
                printf("Case #%d: RICHARD\n",j);
        }
        else if(x>=7)
            printf("Case #%d: RICHARD\n",j);
        else
        {
            if((r*c%x==0) && (abs(r-c)<=1) && (r==x || c==x))
                printf("Case #%d: GABRIEL\n",j);
            else
                printf("Case #%d: RICHARD\n",j);
        }
    }
    return 0;
}


