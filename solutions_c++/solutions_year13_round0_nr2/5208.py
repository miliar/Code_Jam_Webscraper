#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std ;
#define N 109

int a[N][N] ;
int t, cas, n, m ;

bool is_block ( int x, int y){
  bool xxx = true , yyy = true ;
  for ( int i = x ; i < n ; ++i ) {
    if ( a[i][y] > a[x][y] ){
      xxx = false ;
    }
  }
  for ( int i = x ; i >= 0 ; --i ) {
    if ( a[i][y] > a[x][y] ){
      xxx = false ;
    }
  }
  for ( int j = y ; j < m ; ++j ) {
    if ( a[x][j] > a[x][y] ){
      yyy = false ;
    }
  }
  for ( int j = y ; j >= 0 ; --j ) {
    if ( a[x][j] > a[x][y] ){
      yyy = false ;
    }
  }
  return ! ( xxx || yyy ) ;
}
int main () {
  //freopen( "B-small-attempt1.in", "r", stdin );
  //freopen( "B-small.out", "w", stdout );
  freopen( "B-large.in", "r", stdin );
  freopen( "B-large.out", "w", stdout );

  scanf ( "%d", &t ) ;
  for ( cas = 1 ; cas <= t ; ++cas ) {
    scanf ( "%d %d" , &n, &m ) ;
    for ( int i = 0 ; i < n ; ++i ) {
      for ( int j = 0 ; j < m ; ++j ) {
        scanf ( "%d", &a[i][j] ) ;
      }
    }
    printf ( "Case #%d: ", cas ) ;
    bool nonono = false ;
    for ( int i = 0 ; i < n ; ++i ) {
      if ( nonono ) break ;
      for ( int j = 0 ; j < m ; ++j ){
        if ( is_block ( i, j ) ) {
          printf ( "NO" ) ;
          nonono = true ;
          break ;
        }
      }
    }
    if ( !nonono )  printf ( "YES" );
    printf ( "\n" );
  }

}
