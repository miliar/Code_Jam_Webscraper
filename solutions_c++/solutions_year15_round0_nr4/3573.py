#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int w=1;w<=t;w++)
    {
        int x,r,c,p;
        scanf("%d%d%d",&x,&r,&c);
        if(r>c)
        {
            int z=r;
            r=c;
            c=z;
        }
        p=r*c;
        if(x==1)
         printf("Case #%d: GABRIEL\n",w);
        else if(x==2)
        {
            if((r>1||c>1)&&p%x==0)
                printf("Case #%d: GABRIEL\n",w);
                else
                printf("Case #%d: RICHARD\n",w);    
        }
        else if(p%x!=0||x>=(2*r+1)||(x>=(c+r-2)&&x>3))
            printf("Case #%d: RICHARD\n",w);
        else if(x>r&&x>c)
            printf("Case #%d: RICHARD\n",w);
        else printf("Case #%d: GABRIEL\n",w);
    }
    return 0;
}
