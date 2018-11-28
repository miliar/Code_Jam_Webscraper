#include <cstdio>
#include <cmath>

using namespace std;

int main() {
    freopen( "a.in", "r", stdin );
    freopen( "a.out", "w", stdout );
    int T, i, prev, r, t;
    int array[ 1000001 ], sums[ 1000001 ];
    array[ 1 ] = 1;
    sums[ 1 ] = 1;
    for ( i = 2; i <= 1000000; ++i ) {
        array[ i ] = pow( i, 2 ) - sums[ i - 1 ];
        sums[ i ] = sums[ i - 1 ] + array[ i ];
    }
    scanf( "%d", &T );
    for ( int j = 1; j <= T; ++j ) {
        scanf( "%d%d", &r, &t );
        ++r;
        int count = 0;
        while ( t > 0 ) {
            t -= array[ r ];
            r += 2;
            if ( t >= 0 ) { 
                ++count;
            }
        }
        printf( "Case #%d: %d\n", j, count );
    }
    return 0;
}
