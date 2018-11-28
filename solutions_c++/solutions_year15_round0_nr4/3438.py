#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
int main()
{
    int t,x,r,c,i;
    sd(t);
    for(i=1;i<=t;i++)
    {
        sd(x);
        sd(r);
        sd(c);
        if(r*c>=x*(x-1)&&(r*c)%x==0)
            printf("Case #%d: GABRIEL\n",i);
        else
            printf("Case #%d: RICHARD\n",i);
    }
    return 0;
}
