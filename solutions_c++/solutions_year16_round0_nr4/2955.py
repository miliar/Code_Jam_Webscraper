#include <iostream>
#include<stdio.h>
#define ll long long int
//#include<math.h>
using namespace std;
ll power(ll x, ll y)
{
    ll temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}
int main()
{
    //freopen("input3.in","r",stdin);
    //freopen("output3.txt","w",stdout);
    ll t,k,c,s,i=1;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld%lld%lld",&k,&c,&s);
        printf("Case #%lld: ",i);
        i++;
        if(k%2==0)
        {
            ll x=k/2;
            ll siz=power(k,c);
            for(ll i=1; i<=x; i++) printf("%lld ",i);
            for(ll i=siz; i>=(siz-x+1); i--) printf("%lld ",i);
            printf("\n");
        }
        else
        {
            ll x=k/2;
            ll siz=power(k,c);
         //   printf("%lld\n",siz);
            for(ll i=1; i<=x+1; i++) printf("%lld ",i);
            for(ll i=siz; i>=(siz-x+1); i--) printf("%lld ",i);
            printf("\n");
        }
    }
    return 0;
}
