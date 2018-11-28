#include <stdio.h>
#include <algorithm>

int N, X;

int data[ 10003 ];

int main() {
    int T;
    scanf( "%d", &T );

    for( int test = 1; test <= T; test ++ ) {
        scanf( "%d %d", &N, &X );
        for( int i = 1; i <= N; i ++ ) {
            scanf( "%d", &data[ i ] );
        }
        std::sort( data + 1, data + N + 1 );

        int res = 0;
        for( int i = N; i >= 1; i -- ) {
            if( data[ i ] == 0 ) {
                continue;
            }
            res ++;
            for( int j = i - 1; j >= 1; j -- ) {
                if( data[ j ] == 0 ) {
                    continue;
                }
                if( data[ i ] + data[ j ] <= X ) {
                    data[ j ] = 0;
                    break;
                }
            }
        }
        printf( "Case #%d: %d\n", test, res );
    }
    return 0;
}
