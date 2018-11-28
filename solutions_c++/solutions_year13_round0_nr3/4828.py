#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
            int a,b;
            scanf("%d%d",&a,&b);
            int c=0;
            if((a<=1)&&(1<=b))
                   c++;
            if((a<=4)&&(4<=b))
                   c++;
            if((a<=9)&&(9<=b))
                   c++;
            if((a<=121)&&(121<=b))
                   c++;
            if((a<=484)&&(484<=b))
                   c++;
            printf("Case #%d: %d\n",tt,c);
    }
    return 0;
}
