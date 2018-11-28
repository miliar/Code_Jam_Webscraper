#include <cstdio>
#include <cstring>

using namespace std;

int T, K, C, R, S [ 18 ], sol, NoS;

int main ( void ) {
    scanf ( "%d", &T );
    K = T;
    while ( K-- ) {
        scanf ( "%d", &R );
        for ( int i = 0; i < 4; ++i ) {
            for ( int j = 0; j < 4; ++j ) {
                scanf ( "%d", &C );
                if ( i == R - 1 ) ++S [ C ];
            }
        }
        scanf ( "%d", &R );
        for ( int i = 0; i < 4; ++i ) {
            for ( int j = 0; j < 4; ++j ) {
                scanf ( "%d", &C );
                if ( i == R - 1 ) ++S [ C ];
            }
        }
        NoS = 0;
        for ( int i = 1; i <= 16; ++i ) {
            if ( S [ i ] == 2 ) {
                ++NoS;
                sol = i;
            }
        }
        printf ( "Case #%d: ", T - K );
        if ( NoS == 1 ) printf ( "%d\n", sol ); else if ( NoS == 0 ) printf ( "Volunteer cheated!\n" ); else printf ( "Bad magician!\n" );
        memset ( S, 0, sizeof S );
    }
    return 0;
}
