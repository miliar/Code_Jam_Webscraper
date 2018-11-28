#include <iostream>
#include <set>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int cas, row[ 2 ];
int num[ 2 ][ 4 ][ 4 ];
set<int> is;
int main()
{
    freopen( "A-small-attempt2.in", "r",stdin );
    freopen( "A-small-attempt6.out", "w", stdout );
    int cnt = 0;
    scanf( "%d", &cas );
    while ( cas-- )
    {
        int ans = -1, fq = 0;
        scanf( "%d", &row[ 0 ] );
        //is.clear();
        //memset( is, 0, sizeof( is ) );
        for ( int i = 0; i < 4; i++ )
          for ( int j = 0; j < 4; j++ )
          scanf( "%d", &num[ 0 ][ i ][ j ] );
        //for ( int i = 0; i < 4; i++ )
           // is.insert( num[ row - 1 ][ i ]);
        scanf( "%d", &row[ 1 ] );
        for ( int i = 0; i < 4; i++ )
          for ( int j = 0; j < 4; j++ )
          scanf( "%d", &num[ 1 ][ i ][ j ] );
        // if ( row[ 0 ] < 0 || row[ 0 ] > 4 || row[ 1 ] < 0 || row[ 1 ] > 4 )
        // {
          //  printf( "Case #%d: Volunteer cheated!\n", ++cnt );
            //continue;
         //}
         for ( int j = 0; j < 4; j++ )
         for ( int i = 0; i < 4; i++ )
            if ( num[ 0 ][ row[ 0 ] - 1 ][ j ] == num[ 1 ][ row[ 1 ] - 1 ][ i ] )
            {
               // if ( ans == -1 )
                ans = num[ 0 ][ row[ 0 ] -1 ][ j ];
               fq++;
            }
        if ( fq == 1 )
        {
            printf( "Case #%d: %d\n", ++cnt, ans );
        }
        else if ( fq > 1 )
        {
            printf( "Case #%d: Bad magician!\n", ++cnt );
        }
        else
        {
            printf( "Case #%d: Volunteer cheated!\n", ++cnt );
        }
    }


    return 0;
}
