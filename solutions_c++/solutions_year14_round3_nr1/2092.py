#include<stdio.h>
#include<iostream>
using namespace std;

/*
long long int gcd(long long int a, long long int b){ return (b==0) ? a : gcd(b,a%b);}

long long int anc(long long int P,long long int Q)
{
    if(Q & (Q-1))
    return 0;

    if((P/Q)==1)
    return 1;

    return 1+anc(P,Q/2);
}
*/
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    #endif

    int T,test;
    long long int P,Q,ans,tmp;
    scanf("%d",&T);
    for(test=1;test<=T;test++)
    {
        tmp=0;
        ans=0;
        scanf("%lld/%lld",&P,&Q);
        tmp=Q;
        while(tmp!=0)
        {
            if(tmp%2 && tmp!=1)
            break;
            else
            tmp/=2;
        }
        if(tmp!=0)
        printf("Case #%d: impossible\n",test);
        else
        {
            while(P<Q)
            {
                Q/=2;
                ans++;
            }
        printf("Case #%d: %d\n",test,ans);
        }
    }
    return 0;
}

