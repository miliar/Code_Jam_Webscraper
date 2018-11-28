#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


long long int gcd(long long int x,long long int y)
{
    while ( x>0 && y>0)
    {
        if ( x >= y ) x %= y;
        else y %= x;
    }
    return x+y;
}


void solve()
{

    long long int a,b;
    scanf("%lld/%lld",&a,&b);

    if ( a == 0 )
    {
        printf("impossible\n");
        return;
    }
    long long int po = 1;
    long long int o = 0;

    long long int g = gcd(a,b);
    
    a /= g;
    b /= g;

    long long int oka = 1;
    
        while ( po <= a )
        {

            if ( po <= a )
            {
                oka = o;
            }
            po *= 2 ;
            o++;
        } 

    po = 1 ;
    o = 0;

    long long int okb = -1;

        while ( po <= b )
        {

            if ( po == b )
            {
                okb = o;
            }
            po *= 2 ;
            o++;
        } 

    if ( okb == -1 )
        printf("impossible\n");
    else
        printf("%lld\n",okb-oka);
}


int main()
{

    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }

}
