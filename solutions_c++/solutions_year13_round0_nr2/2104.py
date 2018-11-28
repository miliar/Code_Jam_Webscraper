#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#define TRAP assert ( 0 )

int b [ 101 ] [ 101 ];
int row, col;

void _print ( void )
{
    for ( int i = 0; i < row; i++ )
    {
        for ( int j = 0; j < col; j++ )
            printf ( "%d ", b [ i ] [ j ] == INT_MAX ? 0 : b [ i ] [ j ] );
        printf ( "\n" );
    }
    printf ( "\n" );
}

void Load ( void )
{
    memset ( b, 0, sizeof ( b ) );

    scanf ( "%d %d", & row, & col );
    for ( int i = 0; i < row ; i ++ )
        for ( int j = 0; j < col; j ++ )
            scanf ( "%d", & b [ i ] [ j ] );
}

int findMin ( int & r, int & c )
{
    int min = INT_MAX;

    for ( int i = 0; i < row; i ++ )
        for ( int j = 0; j < col; j ++ )
        {
            if ( min > b [ i ] [ j ] )
            {
                min = b [ i ] [ j ];
                r = i;
                c = j;
            }
        }

    return min;
}

void DelRow ( int r )
{
    for ( int i = 0; i < col; i++ )
        b [ r ] [ i ] = INT_MAX;
}
void DelCol ( int c )
{
    for ( int i = 0; i < row; i++ )
        b [ i ] [ c ] = INT_MAX;
}

bool checkRow ( int r, int min )
{
    for ( int i = 0; i < col; i++ )
    {
        if ( b [ r ] [ i ] == INT_MAX )
            continue;
        if ( b [ r ] [ i ] != min )
            return false;
    }
    return true;
}
bool checkCol ( int c, int min )
{
    for ( int i = 0; i < row; i++ )
    {
        if ( b [ i ] [ c ] == INT_MAX )
            continue;
        if ( b [ i ] [ c ] != min )
            return false;
    }

    return true;
}

bool Solve ( void )
{
    Load ( );
    // _print ( );
    while ( true )
    {
        int r, c;
        int min = findMin ( r, c );

        // printf ( "M:%d [%d;%d]\n", min, r, c );
        if ( min == INT_MAX )
            return true;


        // check if row    is all made by min

        bool cr, cc;
        cr = checkRow ( r, min );
        cc = checkCol ( c, min );
        // if ( !cr ) printf ( "CR fail. ");
        // if ( !cc ) printf ( "CC fail. "); else DelCol ( c );
        // printf ( "\n");

        if ( cr )
            DelRow ( r );
        if ( cc )
            DelCol ( c );
        if ( ! cr && ! cc )
            return false;
        // _print ( );
    }

    return true;
}

int main ( void )
{
    int casesCnt;
    scanf ( "%d\n", & casesCnt );

    for ( int i = 1; i <= casesCnt; i++ )
        printf ( "Case #%d: %s\n", i, Solve ( ) ? "YES" : "NO" );
    return EXIT_SUCCESS;
}
