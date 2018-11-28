#include <cstdio>
#include <cstdlib>
#include <cstring>


char str [ 102 ];
int n, L;


bool checkCons ( int a, int b )
{
    int cons = 0;

    for ( int i = a; i <= b; i++ )
    {
        if ( str [ i ] == 'a' || str [ i ] == 'e' || str [ i ] == 'i' || str [ i ] == 'o' || str [ i ] == 'u' )
        {
            cons = 0;
            continue;
        }
        cons += 1;

        if ( cons == n )
        {
            return true;
        }
    }

    return false;
}

int Solve ( void )
{
    memset ( str, 0, sizeof ( str ) );
    scanf ( "\n%s %d", str, & n );
    L = strlen ( str );

    int cnt = 0;
    bool found;

    for ( int i = 0; i < L; i ++ )
    {
        found = false;

        for ( int j = i; j < L; j ++ )
        {
            // substr str[i] ... str [j]
            if ( checkCons ( i, j ) )
                found = true;

            if ( found ) cnt += 1;
        }
    }

    return cnt;
}


int main ( void )
{
    int T;
    scanf ( "%d", & T );

    for ( int i = 1; i <= T; i++ )
        printf ( "Case #%d: %d\n", i, Solve ( ) );

    return EXIT_SUCCESS;
}
