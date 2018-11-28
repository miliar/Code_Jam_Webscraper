#include <cstdio>
using namespace std;

int main() {
    int T, A, B, K;

    freopen( "input.in", "r", stdin );
    freopen( "output.out", "w", stdout );

    scanf( "%d", &T );
    for( int t = 1; t <= T; t++ ) {
        scanf( "%d %d %d", &A, &B, &K );

        int ans = 0;
        for( int i = 0; i < A; i++ )
            for( int j = 0; j < B; j++ )
                if( ( i & j ) < K && ( i & j ) >= 0 )
                    ans++;

        printf( "Case #%d: %d\n", t, ans );
    }

    fclose( stdin );
    fclose( stdout );

    return 0;
}
