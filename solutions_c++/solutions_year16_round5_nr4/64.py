//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , l ;
char g[ 105 ][ 55 ] ;
char b[ 105 ] ;
bool bad ;

void init() {
  bad = false ;
  scanf( "%d%d" , &n , &l ) ;
  for ( int i = 0 ; i < n ; i ++ ) {
    scanf( "%s" , g[ i ] ) ;
    bool n0 = true ;
    for ( int j = 0 ; j < l ; j ++ ) if ( g[ i ][ j ] == '0' )
      n0 = false ;
    if ( n0 ) bad = true ;
  }
  scanf( "%s" , b ) ;
}

void process() {
  if ( bad ) {
    printf( " IMPOSSIBLE\n" ) ;
    return ;
  }
  if ( l == 1 ) {
    printf( " ? 0\n" ) ;
    return ;
  }
  printf( " " ) ;
  for ( int i = 0 ; i < l - 1 ; i ++ ) printf( "?" ) ;
  printf( " " ) ;
  for ( int i = 0 ; i < 35 ; i ++ ) printf( "10" ) ;
  printf( "?" ) ;
  for ( int i = 0 ; i < 35 ; i ++ ) printf( "10" ) ;
  printf( "\n" ) ;
}

int main() {
  int Cases;
  scanf( "%d" , &Cases ) ;
  for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
    init() ;
    printf( "Case #%d:" , cases ) ;
    process() ;
  }
  return 0 ;
}

