#include <iostream>
#include <cstdio>
using namespace std;
const int MAXN = 1000005;
const long long inf = 10000000;
const int MAXD = 16;

long long Reverse( long long x )
{
    long long y = 0;
    while ( x > 0 )
    {
        y = 10 * y + (x % 10);
        x /= 10;
    }

    return y;
}

long long solve( long long x )
{
    if ( x < 10 ) return x;
    if ( x % 10 == 0 ) return solve( x - 1 ) + 1;

    long long dig[MAXD];
    long long exp[MAXD];

    exp[0] = 1;
    for ( int i = 1; i < MAXD; i++)
        exp[i] = (long long)10 * exp[ i - 1 ];

    int D = 0;
    int CopyX = x;
    while ( x > 0 )
    {
        dig[ D ] = x % 10;
        x /= 10;
        D++;
    }

    long long res = 0;
    long long a = 0 , b = 0;

    for ( int i = 0 ; i < (D + 1 )/ 2; i++)
    {
        a += exp[ i ] * dig[ i ];
    }

    for ( int i = 0; i < D / 2; i++ )
    {
        int j = D - 1 - i;
        b += exp[ i ] * dig[ j ];
    }

    res = a + b - 2;
    if ( b != 1 ) res++;

    return res + solve( exp[D - 1] - 1 ) + 2;
}

long long ans[MAXN];
int main()
{
    freopen("inputA.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    for ( int i = 1; i < MAXN ; i++ )
        ans[ i ] = inf * inf;

    ans[ 1 ] = 1;
    for ( int i = 1; i < MAXN; i++ )
    {
        if ( i + 1 < MAXN )
            ans[ i + 1 ] = min( ans[ i ] + 1 , ans[ i + 1 ] );

        if ( Reverse( i ) < MAXN )
            ans[ Reverse( i ) ] = min( ans[ i ] + 1 , ans[ Reverse( i ) ] );
    }

    for ( int _t = 1; _t <= T; _t++ )
    {
        long long N;
        cin >> N;

        cout << "Case #" << _t << ": " << solve( N ) << endl;
    }

    return 0;
}
