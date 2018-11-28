#include <cstdio>
#include <cstring>

using namespace std;

int sol, A, B, K, L, TP;

int main ( void ) {
    scanf ( "%d", &TP );
    L = TP;
    while ( TP-- ) {
        sol = 0;
        scanf ( "%d %d %d", &A, &B, &K );
        for ( int i = 0; i < A; ++i ) {
            for ( int j = 0; j < B; ++j ) {
                if ( ( i & j ) < K ) ++sol; //else printf ( "%d %d %d\n", i, j, i & j );
            }
        }
        printf ( "Case #%d: %d\n", L - TP, sol );
    }
    return 0;
}
