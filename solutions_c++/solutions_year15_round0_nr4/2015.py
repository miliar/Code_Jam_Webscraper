#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T,x,r,c,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
        {
            printf("Case #%d: GABRIEL\n",t);
            continue;
        }
        k=r*c;
        if(k%x!=0)
        {
            printf("Case #%d: RICHARD\n",t);
            continue;
        }
        if(x==2)
        {
            printf("Case #%d: GABRIEL\n",t);
            continue;
        }
        if(x==3)
        {
            if(r==3)
                r=c,c=3;
            if(r==1)
                printf("Case #%d: RICHARD\n",t);
            else
                printf("Case #%d: GABRIEL\n",t);
            continue;
        }
        if(x==4)
        {
            if(r==2&&c==2)
            {
                printf("Case #%d: RICHARD\n",t);
                continue;
            }
            if(r==4)
                r=c,c=4;
            if(r==4||r==3)
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
            continue;
        }
    }
    return 0;
}

