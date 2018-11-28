#include <cstdio>
#include <cstring>

using namespace std;

int TP, K, dp [ 110 ] [ 110 ], L [ 110 ], n, T, N, sol, Min, tmp;
char A [ 110 ] [ 110 ], B [ 110 ] [ 110 ];

int abs ( int X ) {
    if ( X > 0 ) return X; else return -X;
}

int main ( void ) {
    scanf ( "%d", &TP );
    K = TP;
    while ( TP-- ) {
        memset ( B, 0, sizeof B );
        memset ( dp, 0, sizeof dp );
        memset ( L, 0, sizeof L );
        scanf ( "%d", &N );
        for ( int i = 0; i < N; ++i ) {
            scanf ( "%s", A [ i ] );
            L [ i ] = strlen ( A [ i ] );
        }
        for ( int i = 0; i < N; ++i ) {
            T = 0;
            for ( int j = 0; j < L [ i ]; ++j ) {
                if ( A [ i ] [ j ] != A [ i ] [ j + 1 ] ) {
                    B [ i ] [ T++ ] = A [ i ] [ j ];
                }
            }
        }
        bool C = 0;
        for ( int i = 1; i < N; ++i ) {
            C = strcmp ( B [ i ], B [ 0 ] );
        }
        printf ( "Case #%d: ", K - TP );
        if ( C ) {
            printf ( "Fegla won\n");
            continue;
        }
        for ( int i = 0; i < N; ++i ) {
            T = 0; n = 1;
            for ( int j = 0; j < L [ i ]; ++j ) {
                if ( A [ i ] [ j ] != A [ i ] [ j + 1 ] ) {
                    dp [ i ] [ T++ ] = n; n = 1;
                } else {
                    ++n;
                }
            }
            dp [ i ] [ T ] = n;
        }
        sol = 0;
        for ( int i = 0; i <= T; ++i ) {
            Min = 1000000000;
            for ( int j = 0; j < N; ++j ) {
                tmp = 0;
                for ( int k = 0; k < N; ++k ) {
                    tmp += abs ( dp [ j ] [ i ] - dp [ k ] [ i ] );
                }
                if ( tmp < Min ) Min = tmp;
            }
            sol += Min;
        }
        printf ( "%d\n", sol );
    }
    return 0;
}
