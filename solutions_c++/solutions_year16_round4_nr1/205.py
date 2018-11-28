//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , s[ 5 ] ;

void init() {
  scanf( "%d" , &n ) ;
  for ( int i = 0 ; i < 3 ; i ++ ) scanf( "%d" , &s[ i ] ) ;
}

// r > s > p
// 0 > 2 > 1

int cnt[ 5 ] ;

bool myless( int x , int y ) {
  if ( x == y ) return false ;
  if ( x == 1 ) return true ;
  if ( y == 1 ) return false ;
  if ( x == 0 ) return true ;
  if ( y == 0 ) return false ;
  return false ;
}

vector< int > DO( int k , int m ) {
  if ( m == 0 ) {
    vector< int > ret ;
    ret.push_back( k ) ;
    return ret ;
  }
  int k2 = ( k + 2 ) % 3 ;
  vector< int > v1 = DO( k , m - 1 ) ;
  vector< int > v2 = DO( k2 , m - 1 ) ;
  bool flg = true ;
  for ( int i = 0 ; i < (int)v1.size() ; i ++ ) {
    if ( myless( v1[ i ] , v2[ i ] ) ) {
      flg = true ; break ;
    } else if ( myless( v2[ i ] , v1[ i ] ) ) {
      flg = false ; break ;
    }
  }
  if ( flg ) {
    for ( int x : v2 ) v1.push_back( x ) ;
    return v1 ;
  } else {
    for ( int x : v1 ) v2.push_back( x ) ;
    return v2 ;
  }
}

void process() {
  for ( int k = 0 ; k < 3 ; k ++ ) {
    cnt[ 0 ] = cnt[ 1 ] = cnt[ 2 ] = 0 ;
    cnt[ k ] = 1 ;
    for ( int i = 0 ; i < n ; i ++ ) {
      int tcnt[ 5 ] ;
      tcnt[ 0 ] = cnt[ 0 ] + cnt[ 1 ] ;
      tcnt[ 1 ] = cnt[ 1 ] + cnt[ 2 ] ;
      tcnt[ 2 ] = cnt[ 2 ] + cnt[ 0 ] ;
      cnt[ 0 ] = tcnt[ 0 ] ;
      cnt[ 1 ] = tcnt[ 1 ] ;
      cnt[ 2 ] = tcnt[ 2 ] ;
    }
    if ( cnt[ 0 ] == s[ 0 ] && cnt[ 1 ] == s[ 1 ] && cnt[ 2 ] == s[ 2 ] ) {
      vector< int > ans = DO( k , n ) ;
      for ( int x : ans ) {
        if ( x == 0 ) putchar( 'R' ) ;
        else if ( x == 1 ) putchar( 'P' ) ;
        else if ( x == 2 ) putchar( 'S' ) ;
      }
      puts( "" ) ;
      return ;
    }
  }
  puts( "IMPOSSIBLE" ) ;
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

