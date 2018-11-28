#include <cstdio>

using namespace std;

int n, m;

bool check( int field[][ 100 ], int line, int col ) {
    int num = field[ line ][ col ], i, j;
    bool found = false;
    for ( i = 0; i < m; ++i ) {
        if ( field[ line ][ i ] > num ) {
            found = true;
            break;
        }
    }
    if ( !found ) {
        return false;
    }
    found = false;
    for ( i = 0; i < n; ++i ) {
        if ( field[ i ][ col ] > num ) {
            found = true;
            break;
        }
    }
    if ( !found ) {
        return false;
    }
    return true;
}

int main() {
    freopen( "b.in", "r", stdin );
    freopen( "b.out", "w", stdout );
    int t, i, j, k;
    int field[ 100 ][ 100 ];
    scanf( "%d", &t );
    for ( k = 1; k <= t; ++k ) {
        scanf( "%d%d", &n, &m );
        for ( i = 0; i < n; ++i ) {
            for ( j = 0; j < m; ++j ) {
                scanf( "%d", field[ i ] + j );
            }
        }
        bool found = false;
        for ( i = 0; i < n; ++i ) {
            for ( j = 0; j < m; ++j ) {
                if ( check( field, i, j ) ) {
                    found = true;
                    break;
                }
            }
            if ( found ) {
                break;
            }
        }
        if ( !found ) {
            printf( "Case #%d: YES\n", k );
        }
        else {
            printf( "Case #%d: NO\n", k );
        }
    }
    return 0;
}
