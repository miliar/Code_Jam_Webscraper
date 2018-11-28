#include <cstdio>

using namespace std;

int rev( int num ) {
    int sol = 0;
    while ( num > 0 ) {
        sol = ( sol * 10 ) + ( num % 10 );
        num /= 10;
    }
    return sol;
}

bool pal( int num ) {
    int revised = rev( num );
    if ( revised == num ) {
        return true;
    }
    return false;
}

int main() {
    freopen( "c.in", "r", stdin );
    freopen( "c.out", "w", stdout );
    int t, beg, lim, count, i, sqrt, j;
    scanf( "%d", &t );
    for ( i = 1; i <= t; ++i ) {
        scanf( "%d%d", &beg, &lim );
        count = 0;
        while ( beg <= lim ) {
            sqrt = 0;
            for ( j = 1; j <= beg; ++j ) {
                if ( j * j == beg ) {
                    sqrt = j;
                }
            }
            if ( sqrt != 0 && pal( beg ) && pal( sqrt ) ) {
                ++count;
            }
            ++beg;
        }
        printf( "Case #%d: %d\n", i, count );
    }
    return 0;
}
