#include <iostream>
#include <stdio.h>
using namespace std ;

int main () {
  freopen( "A-small.in", "r", stdin );
  freopen( "A.out", "w", stdout );
  
  int t, n, cas, p, q ;
  int fst[4][4], secd[4][4] ;

  scanf ( "%d" , &t );
  for ( cas = 1 ; cas <= t ; ++cas ){
    
    scanf ( "%d", &p );
    --p;
    for ( int i = 0 ; i < 4 ; ++i ) {
      for ( int j = 0 ; j < 4 ; ++j ) {
        scanf ( "%d", &fst[i][j] );
      }
    }
    
    scanf ( "%d", &q );
    --q;
    for ( int i = 0 ; i < 4 ; ++i ) {
      for ( int j = 0 ; j < 4 ; ++j ) {
        scanf ( "%d", &secd[i][j] );
      }
    }
    
    // output
    printf ( "Case #%d: ", cas );
    
    int sameCnt = 0, ans = -1;
    for ( int i = 0 ; i < 4; ++i ) {
      for ( int j = 0 ; j < 4 ; ++j ) {
        if ( fst[p][i] == secd[q][j] ) {
          ++sameCnt ;
          ans = fst[p][i] ;
        }
      }
    }
    if ( sameCnt == 0 ) {
      printf ( "Volunteer cheated!\n" );
    }
    else if ( sameCnt > 1 ) {
      printf ( "Bad magician!\n" ) ;
    }
    else {
      printf ( "%d\n", ans ) ;
    }
  }
}
