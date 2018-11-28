#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,x,r,c;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        scanf("%d%d%d",&x,&r,&c);
        
        if((r*c)%x!=0)
        {
            printf("Case #%d: RICHARD\n",tt);
            continue;
        }
        
        else
        {
            int f=0;
            for(int i=1;i<=x;i++)
            {

                {
                    if(!(min(i,x-i+1)<=min(r,c) && max(i,x-i+1)<=max(r,c)))
                    {
                        f=1;break;
                    }
                }
            }
            if(f)printf("Case #%d: RICHARD\n",tt);
            else
            {
                if(x==4 && min(r,c)==2 && max(r,c)==4)
                    printf("Case #%d: RICHARD\n",tt);
                else printf("Case #%d: GABRIEL\n",tt);
            } 
        }
    }
    return 0;
}

