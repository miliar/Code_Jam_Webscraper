#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <climits>

long int A, N, M [ 101 ], g [ 101 ];

#define REST(i) ( N - (i) - 1 )
using std ::min;

void Solve ( int caseId )
{
    A = N = 0;
    memset ( g, 0, sizeof ( g ) );

    scanf ( "%ld %ld", & A, & N );
    for ( int i = 0; i < N; i++ )
        scanf ( "%ld", & M [ i ] );

    std :: sort ( M, M + N );

    // printf ( "%d | %d ||| ", A, N );
    // for ( int i = 0; i < N; i++ )
    //     printf ( "%d, ", M [ i ] );
    // printf ( "\n" );

    long int best = INT_MAX, inc = 0;

    for ( int i = 0; i < N; i++ )
    {
        while ( A <= M [ i ] )
        {
            if ( A - 1 == 0 ) // impossible
            {
                printf ( "Case #%d: %ld\n", caseId, std :: min ( N - i, N ) );
                return;
            }

            A += A - 1;
            inc ++;
        }

        A += M [ i ];

        //printf ( "I:%d, Best: %d, Inc:%d, Rest:%d A:%d ", i, best, inc, REST(i), A );
        best = min ( inc + REST(i), best );
        //printf ( "NBest: %d\n", best );
    }

    printf ( "Case #%d: %ld\n", caseId, std :: min ( best, N ) );
}

int main ( void )
{
    int casesCnt;
    scanf ( "%d", & casesCnt );
    for ( int i = 1; i <= casesCnt; i++ )
        Solve ( i );

    return EXIT_SUCCESS;
}
