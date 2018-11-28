#include <cstdio>
#include <iostream>

using namespace std;

int matrix1[4][4], matrix2[4][4];

void solution( int A, int B, int count )
{
     int n = 0, ans = 0;
     for( int i=0; i<4; i++ )
          for( int j=0; j<4; j++ )
          {
               if( matrix1[A][i] == matrix2[B][j] )
               {
                   n++;
                   if( n > 1 )
                   {
                       printf( "Case #%d: Bad magician!\n", count );
                       return;
                   }
                   ans = matrix2[B][j];
               }
          }
     if( n == 1 )
         printf( "Case #%d: %d\n", count, ans );
     else
         printf( "Case #%d: Volunteer cheated!\n", count );              
}

int main()
{
    freopen( "A-small-attempt0.in", "r", stdin );
    freopen( "outputmagic.txt", "w", stdout );
    int T, count = 1;
    scanf( "%d", &T );
    while( T-- )
    {
           int A, B;
           scanf( "%d", &A );
           for( int i=0; i<4; i++ )
                for( int j=0; j<4; j++ )
                     scanf( "%d", &matrix1[i][j] );
           scanf( "%d", &B );
           for( int i=0; i<4; i++ )
                for( int j=0; j<4; j++ )
                     scanf( "%d", &matrix2[i][j] );
           solution( --A, --B, count++ );
    }
}
