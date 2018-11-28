#include <iostream>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {
    int T, N;
    double b;

    FILE *fin, *fout;
    fin = fopen("input.in", "r");
    fout = fopen("output.out", "w");

    //cin >> T;
    fscanf( fin, "%d", &T );
    for( int t = 1; t <= T; t++ ) {
        // cin >> N;
        fscanf( fin, "%d", &N );
        set< double > n1, n2, k1, k2;
        for( int i = 0; i < N; i++ ) {
            //cin >> b;
            fscanf( fin, "%lf", &b );
            n1.insert( b );
            n2.insert( b );
        }
        for( int i = 0; i < N; i++ ) {
            //cin >> b;
            fscanf( fin, "%lf", &b );
            k1.insert( b );
            k2.insert( b );
        }

        // WAR
        int scoreWar = 0;
        set< double >::iterator in, ik;
        while( !n1.empty() ) {
              in = n1.begin();
              ik = k1.upper_bound( *in );
              if( ik == k1.end() ) {
                    scoreWar++;
                    ik = k1.begin();
              }
              n1.erase( in );
              k1.erase( ik );
        }

        // DECEITFUL WAR
        int scoreDec = 0;
        while( !k2.empty() ) {
              ik = k2.end();
              --ik;
              in = n2.upper_bound( *ik );
              if( in != n2.end() )
                    scoreDec++;
              else
                    in = n2.begin();
              n2.erase( in );
              k2.erase( ik );
        }

        //cout << "Case #" << t << ": " << scoreDec << " " << scoreWar << endl;
        fprintf( fout, "Case #%d: %d %d\n", t, scoreDec, scoreWar );
    }

    return 0;
}
