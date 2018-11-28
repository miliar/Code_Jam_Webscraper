//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n ;
int s[ 5 ][ 5 ] ;
int d[ 5 ][ 5 ] ;

void init() {
  scanf( "%d" , &n ) ;
  for ( int i = 0 ; i < n ; i ++ ) {
    char buf[ 50 ] ;
    scanf( "%s" , buf ) ;
    for ( int j = 0 ; j < n ; j ++ ) {
      s[ i ][ j ] = buf[ j ] - '0' ;
    }
  }
}
int ans ;
int order[ 5 ] ;
int usd[ 5 ] ;

bool nogood( int nw ) {
  if ( nw == n ) return false ;
  bool gd = false ;
  for ( int i = 0 ; i < n ; i ++ ) if ( usd[ i ] == false && d[ order[ nw ] ][ i ] ) {
    gd = true ;
    usd[ i ] = true ;
    if ( nogood( nw + 1 ) ) return true ;
    usd[ i ] = false ;
  }
  if ( gd == false ) return true ;
  return false ;
}

bool mtry() {
  bool ok = true ;
  for ( int i = 0 ; i < n ; i ++ ) order[ i ] = i ;
  do {
    for ( int i = 0 ; i < n ; i ++ ) usd[ i ] = false ;
    if ( nogood( 0 ) ) ok = false ;
  } while ( next_permutation( order , order + n ) ) ;
  return ok ;
}

void process() {
  ans = n * n ;
  for ( int i = 0 ; i < ( 1 << ( n * n ) ) ; i ++ ) {
    for ( int j1 = 0 ; j1 < n ; j1 ++ )
      for ( int j2 = 0 ; j2 < n ; j2 ++ )
        d[ j1 ][ j2 ] = s[ j1 ][ j2 ] ;
    bool flg = true ;
    int cnt = 0 ;
    for ( int j = 0 ; j < ( n * n ) ; j ++ ) if ( i & ( 1 << j ) ) {
      int j1 = j / n , j2 = j % n ;
      if ( d[ j1 ][ j2 ] == 1 ) {
        flg = false ;
        break ;
      }
      d[ j1 ][ j2 ] = 1 ;
      cnt ++ ;
    }
    if ( flg ) {
      //printf( "%d\n" , i ) ;
    //for ( int j1 = 0 ; j1 < n ; j1 ++ ) {
      //for ( int j2 = 0 ; j2 < n ; j2 ++ ) 
        //printf( "%d" , d[ j1 ][ j2 ] ) ;
      //puts( "" ) ;
    //}
      if ( mtry() ) ans = min( ans , cnt ) ;
    }
  }
  printf( "%d\n" , ans ) ;
}

int main() {
  int Cases;
  scanf( "%d" , &Cases ) ;
  for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
    init() ;
    printf( "Case #%d: " , cases ) ;
    process() ;
  }
  return 0 ;
}

