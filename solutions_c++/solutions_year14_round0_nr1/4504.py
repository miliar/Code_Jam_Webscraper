#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int m1[ 16 ][ 16 ], m2[ 16 ][ 16 ];

int numInter( int r1, int r2, int *card ) {
    int ans = 0;
    for( int j = 0; j < 4; j++ )
        for( int k = 0; k < 4; k++ )
            if( m1[ r1 ][ j ] == m2[ r2 ][ k ] ) {
                ans++;
                *card = m1[ r1 ][ j ];
            }
    return ans;
}

int main() {
    int r1, r2, T, card;

    FILE *fin, *fout;
    fin = fopen("input.in", "r");
    fout = fopen("output.out", "w");

    fscanf( fin, "%d", &T );
    for( int t = 1; t <= T; t++ ) {
        fscanf( fin, "%d", &r1 );
        r1--;
        for( int i = 0; i < 4; i++ )
            for( int j = 0; j < 4; j++ )
                fscanf( fin, "%d", &m1[ i ][ j ] );
        fscanf( fin, "%d", &r2 );
        r2--;
        for( int i = 0; i < 4; i++ )
            for( int j = 0; j < 4; j++ )
                fscanf( fin, "%d", &m2[ i ][ j ] );

        fprintf( fout, "Case #%d: ", t );
        int ans = numInter( r1, r2, &card );
        if( ans == 1 )
            fprintf( fout, "%d\n", card );
        else if( ans == 0 )
            fprintf( fout, "Volunteer cheated!\n" );
        else
            fprintf( fout, "Bad magician!\n" );
    }

    return 0;
}
