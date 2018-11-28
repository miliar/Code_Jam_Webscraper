#include <stdio.h>
#include <string.h>

int N, M, res, rescnt, full_length;

int L[ 1003 ];
int server[ 1003 ];

int D[ 1003 ][ 1003 ];

char data[ 1003 ][ 103 ];


int calc() {
    int s = full_length;
    int chk[ 103 ] = { 0, };

    for( int i = 1; i <= M; i ++ ) {
        chk[ server[ i ] ] = 1;
        int mx = 0;
        for( int j = 1; j < i; j ++ ) {
            if( server[ i ] == server[ j ] && mx < D[ i ][ j ] ) {
                mx = D[ i ][ j ];
            }
        }
        s -= mx;
    }
    for( int i = 1; i <= N; i ++ ) {
        s += chk[ i ];
    }
    return s;
}

void back( int now ) {
    if( now == M + 1 ) {
        int tmp = calc();
        if( tmp > res ) {
            res = tmp;
            rescnt = 1;
        } else if( tmp == res ) {
            rescnt ++;
        }
    } else {
        for( int i = 1; i <= N; i ++ ) {
            server[ now ] = i;
            back( now + 1 );
        }
    }
}

int prefix( int a, int b ) {
    int ret = 0;
    for( int i = 1; i <= L[ a ] && L[ b ]; i ++ ) {
        if( data[ a ][ i ] != data[ b ][ i ] ) {
            break;
        }
        ret = i;
    }
    return ret;
}

int main() {
    int T;
    scanf( "%d", &T );

    for( int test = 1; test <= T; test ++ ) {
        scanf( "%d %d", &M, &N );

        full_length = 0;

        for( int i = 1; i <= M; i ++ ) {
            scanf( "%s", data[ i ] + 1 );
            L[ i ] = strlen( data[ i ] + 1 );
            full_length += L[ i ];

            for( int j = 1; j < i; j ++ ) {
                D[ i ][ j ] = D[ j ][ i ] = prefix( i, j );
            }
        }

        res = 0;
        rescnt = 0;
        back( 1 );
        printf( "Case #%d: %d %d\n", test, res, rescnt );
    }
    return 0;
}
