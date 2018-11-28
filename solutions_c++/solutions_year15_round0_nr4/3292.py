#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("dsmall.txt","r",stdin);
    freopen("odsmall.txt","w",stdout);
    int t,i,j;

    int x,r,c;

    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        //printf("%d %d:   ",(int)ceil(x*1.0/2),min(r,c));
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
            if(min(r,c)>1 && (r*c)%3==0)
                printf("Case #%d: GABRIEL\n",i);
            else
                printf("Case #%d: RICHARD\n",i);
        }
        else
        {
            if(min(r,c)>2 && (r*c)%4==0)
                printf("Case #%d: GABRIEL\n",i);
            else
                printf("Case #%d: RICHARD\n",i);
        }

    }
}
