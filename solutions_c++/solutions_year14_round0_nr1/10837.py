#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
    int T, t = 0;
    freopen( "A-small-attempt2.in", "r", stdin );
    freopen( "A-small.out", "w", stdout );
    scanf( "%d", &T );
    while( T-- )
    {
        int n1, n2;
        int Num1[ 20 ] = {0};
        int Num2[ 20 ] = {0};
        int tmp[ 4 ][ 4 ] = {0};
        scanf( "%d", &n1 );
        for( int i = 0; i < 4; i++) {
            for( int j = 0; j < 4; j++ ) {
                scanf( "%d", &tmp[ i ][ j ] );
                if( i == n1-1 )
                    Num1[ tmp[ i ][ j ] ] = 1;
                else
                    Num1[ tmp[ i ][ j ] ] = 0;
            }
        }
        scanf( "%d", &n2 );
        for( int i = 0; i < 4; i++) {
            for( int j = 0; j < 4; j++ ) {
                scanf( "%d", &tmp[ i ][ j ] );
                if( i == n2-1 )
                    Num2[ tmp[ i ][ j ] ] = 1;
                else
                    Num2[ tmp[ i ][ j ] ] = 0;
            }
        }
        int Check = 0, ans = -1;
        for( int i = 1; i <= 16; i++ )
            if( Num1[ i ] & Num2[ i ] == 1 )
                Check++, ans = i;
        if( Check == 1 )
            printf( "Case #%d: %d\n", ++t, ans );
        else if( Check > 1 )
            printf( "Case #%d: Bad magician!\n", ++t );
        else
            printf( "Case #%d: Volunteer cheated!\n", ++t );
    }

    return 0;
}
