#include <cstdio>
#include <iostream>

using namespace std;

long long int a , b, ans;

long long int gcd ( long long int g1 , long long int g2 )
{
    return g2 == 0LL ? g1 : gcd(g2,g1%g2);
}


int solve()
{
    if ( a > b ) return 1;
    long long int g = gcd(b,a);
    b = b/g; a = a/g;
    long long int tmpb, digit = 0;
    tmpb = b;
    while ( b != 1LL )
    {
        digit ++;
        if ( b%2 != 0 ) return 1;
        b /= 2;
    }
    b = tmpb;

    if ( a == 1 && b == 1 ) ans = 0;
    else if ( a == 1 ) ans = digit;
    else
    {
        ans = 1;
        while ( a*2 <= b )
        {
            ans ++;
            b = b / 2;
        }
    }
    return 0;
}



int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int t, T;
    char j;
    scanf("%d",&T);
    for ( t = 0 ; t < T ; t ++ )
    {
        scanf("%lld",&a);
        getchar();
        scanf("%lld",&b);

        printf("Case #%d: ",t+1);
        if ( solve() == 1 ) printf("impossible\n");
        else printf("%lld\n",ans);


    }

    return 0;
}
