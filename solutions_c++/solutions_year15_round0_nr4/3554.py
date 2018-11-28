#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    long long int i,t,T,x,r,c,totc;
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%lld %lld %lld",&x,&r,&c);
        totc=r*c;
        if(x==1)
            printf("Case #%lld: GABRIEL\n",t);
        if(x==2)
        {
            if(totc%2==0)
                printf("Case #%lld: GABRIEL\n",t);
            else
                printf("Case #%lld: RICHARD\n",t);
        }
        if(x==3)
        {
            if(totc>=6)
            {
                if(totc%3==0)
                    printf("Case #%lld: GABRIEL\n",t);
                else
                    printf("Case #%lld: RICHARD\n",t);
            }
            else
                printf("Case #%lld: RICHARD\n",t);
        }
        if(x==4)
        {
            if(totc>=12)
            {
                if(totc%4==0)
                    printf("Case #%lld: GABRIEL\n",t);
                else
                    printf("Case #%lld: RICHARD\n",t);
            }
            else
                printf("Case #%lld: RICHARD\n",t);
        }
    }
    return 0;
}
