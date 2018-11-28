//
//  main.cpp
//  codejam
//
//  Created by shawpan on 4/12/14.
//  Copyright (c) 2014 shawpan. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[])
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int c1,c2,t,i,r1,r2,r,n,c,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        c1=c2=0;
        scanf("%d",&r1);
        
        for(r=1;r<17;r++)
        {
            scanf("%d",&n);
            if(r > (r1-1)*4 && r <= r1*4)
            {
                c1 |= (1<<(n-1));
            }
        }
        
        scanf("%d",&r2);
        
        for(r=1;r<17;r++)
        {
            scanf("%d",&n);
            if(r > (r2-1)*4 && r <= r2*4)
            {
                c2 |= (1<<(n-1));
            }
        }
        c = c1 & c2;
        if(c && !(c & (c-1)))
        {
            j=n=1;
            while(!(j & c))
            {
                j <<= 1;n++;
            }
            printf("Case #%d: %d\n",i,n);
        }
        else if(!c)
        {
            printf("Case #%d: Volunteer cheated!\n",i);
            
        }
        else
        {
            printf("Case #%d: Bad magician!\n",i);
        }
    }
    return 0;
}

