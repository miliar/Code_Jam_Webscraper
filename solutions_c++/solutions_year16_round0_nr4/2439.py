#include<bits/stdc++.h>


using namespace std;
#define ll long long int

ll modulo(ll base, ll exponent)
{
    ll x = 1;
    ll y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) ;
        y = (y * y) ;
        exponent = exponent / 2;
    }
    return x ;
}

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("output10.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for(int j=1;j<=t;j++)
    {

        ll k,c,s;
        scanf("%lld %lld %lld",&k,&c,&s);
        printf("Case #%d: ",j);

        ll add=modulo(k,c-1);
        ll sum=1;
        for(ll i=1;i<=s;i++)
        {
            printf("%lld ",sum);
            sum=sum+add;
        }

        printf("\n");
    }

}
