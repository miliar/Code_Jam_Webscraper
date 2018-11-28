#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define MAX 50
#define INF 2000000000

using namespace std;

ll t, n, N, i = 1;
set < ll > s;

int main ( )
{
    ios_base :: sync_with_stdio ( 0 );
    freopen ( "A-large.in", "r", stdin );
    freopen ( "A-large.out", "w", stdout );

    scanf ( "%I64d", &t );

    for ( int k = 0; k < t; ++ k )
    {
        scanf ( "%I64d", &n );

        printf ( "Case #%I64d: ", i++ );

        ll j = 1;
        if ( n == 0 )
        {
            printf ( "INSOMNIA\n" );
            continue;
        } s.clear ( );
        while ( s.size() < 10 )
        {
            N = n*(j++);

            while ( N )
            {
                s.insert ( N%10 );
                N /= 10;
            }
        }
        printf ( "%I64d\n", n*(j-1) );
    }


    return 0;
}
