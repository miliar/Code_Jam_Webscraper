#include <stdio.h>
#include <algorithm>

int N;

int data[ 1003 ];
int sorted[ 1003 ];
int left[ 1003 ];
int right[ 1003 ];

int D[ 1003 ][ 1003 ];

int main() {
    int T;
    scanf( "%d", &T );
    for( int test = 1; test <= T; test ++ ) {
        scanf( "%d", &N );

        for( int i = 1; i <= N; i ++ ) {
            scanf( "%d", &data[ i ] );
            sorted[ i ] = data[ i ];
        }

        std::sort( sorted + 1, sorted + N + 1 );
        for( int i = 1; i <= N; i ++ ) {
            for( int j = 1; j <= N; j ++ ) {
                if( data[ i ] == sorted[ j ] ) {
                    data[ i ] = j;
                    break;
                }
            }
        }
        for( int i = 1; i <= N; i ++ ) {
            left[ i ] = right[ i ] = 0;
            for( int j = 1; j < i; j ++ ) {
                if( data[ i ] < data[ j ] ) {
                    left[ i ] ++;
                }
            }
            for( int j = i + 1; j <= N; j ++ ) {
                if( data[ i ] < data[ j ] ) {
                    right[ i ] ++;
                }
            }
        }
        for( int i = 0; i <= N; i ++ ) {
            for( int j = 0; j <= N; j ++ ) {
                D[ i ][ j ] = 10000000;
            }
        }

        D[ 0 ][ 0 ] = 0;
        for( int i = 0; i < N; i ++ ) {
            for( int j = 0; j < N; j ++ ) {
                int next = i;
                if( next < j ) {
                    next = j;
                }
                next ++;
                if( next > N ) {
                    continue;
                }

                if( D[ next ][ j ] > D[ i ][ j ] + left[ next ] ) {
                    D[ next ][ j ] = D[ i ][ j ] + left[ next ];
                }
                if( D[ i ][ next ] > D[ i ][ j ] + right[ next ] ) {
                    D[ i ][ next ] = D[ i ][ j ] + right[ next ];
                }
            }
        }
        int res = 10000000;
        for( int i = 0; i < N; i ++ ) {
            if( res > D[ i ][ N ] ) {
                res = D[ i ][ N ];
            }
            if( res > D[ N ][ i ] ) {
                res = D[ N ][ i ];
            }
        }

        printf( "Case #%d: %d\n", test, res );
    }

    return 0;
}
