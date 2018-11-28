#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
int main()
{
    int t,k=1,c,x,r;

    sd(t);
    while(t--)
    {
        sd(x);sd(r);sd(c);
        if(x==1)
        printf("Case #%d: GABRIEL\n",k);
        else if(x==2)
        {
            if(r%2!=0 && c%2!=0)
                printf("Case #%d: RICHARD\n",k);
            else
                printf("Case #%d: GABRIEL\n",k);
        }
        else if(x==3)
        {
            if(r==3 && c==3)
                printf("Case #%d: GABRIEL\n",k);
            else if((r==2 && c==3)||(r==3 && c==2) )
                printf("Case #%d: GABRIEL\n",k);
            else if((r==3 && c==4)||(r==4 && c==3))
                printf("Case #%d: GABRIEL\n",k);
            else
                printf("Case #%d: RICHARD\n",k);
        }
        else
        {
            if((r==3 && c==4)||(r==4 && c==3))
                printf("Case #%d: GABRIEL\n",k);
            else if(r==4 && c==4)
                printf("Case #%d: GABRIEL\n",k);
            else
                printf("Case #%d: RICHARD\n",k);
        }
        k++;

    }
    return 0;
}
