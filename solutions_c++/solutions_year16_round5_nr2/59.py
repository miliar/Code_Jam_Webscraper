//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , m ;
int p[ 105 ] ;
int vl[ 105 ] ;
char s[ 105 ] ;
char q[ 10 ][ 105 ] ;
int lnn[ 10 ] ;
vector< int > v[ 105 ] ;

int dfs( int x ) {
  if ( vl[ x ] ) return vl[ x ] ;
  vl[ x ] = 1 ;
  for ( int nxt : v[ x ] )
    vl[ x ] += dfs( nxt ) ;
  return vl[ x ] ;
}

void init() {
  scanf( "%d" , &n ) ;
  for ( int i = 1 ; i <= n ; i ++ )
    v[ i ].clear() , vl[ i ] = 0 ;
  for ( int i = 1 ; i <= n ; i ++ ) {
    scanf( "%d" , &p[ i ] ) ;
    v[ p[ i ] ].push_back( i ) ;
  }
  scanf( "%s" , s + 1 ) ;
  scanf( "%d" , &m ) ;
  for ( int i = 1 ; i <= m ; i ++ ) {
    scanf( "%s" , q[ i ] ) ;
    lnn[ i ] = strlen( q[ i ] ) ;
  }
  for ( int i = 1 ; i <= n ; i ++ ) if ( vl[ i ] == 0 ) {
    dfs( i ) ;
  }
}

int tot ;
int ok[ 10 ] ;
vector< int > pq ;
int vvl[ 105 ] ;
char buf[ 105 ] ;

void process() {
  tot = 0 ;
  for ( int i = 1 ; i <= m ; i ++ ) ok[ i ] = 0 ;
  for ( int k = 0 ; k < 30000 ; k ++ ) {
    pq.clear() ;
    for ( int i = 1 ; i <= n ; i ++ ) {
      if ( p[ i ] == 0 ) {
        pq.push_back( i ) ;
      }
    }
    int ln = 0 ;
    while ( pq.size() > 0 ) {
      for ( int i = 0 ; i < (int)pq.size() ; i ++ )
        vvl[ i ] = vl[ pq[ i ] ] ;
      for ( int i = 1 ; i < (int)pq.size() ; i ++ )
        vvl[ i ] += vvl[ i - 1 ] ;
      int bal = rand() % vvl[ (int)pq.size() - 1 ] ;
      int can = 0 ;
      while ( can < (int)pq.size() && vvl[ can ] <= bal ) can ++ ;
      buf[ ln ++ ] = s[ pq[ can ] ] ;
      for ( int nxt : v[ pq[ can ] ] )
        pq.push_back( nxt ) ;
      pq.erase( pq.begin() + can ) ;
    }
    tot ++ ;
    for ( int j = 1 ; j <= m ; j ++ ) {
      for ( int pt1 = 0 ; pt1 + lnn[ j ] <= ln ; pt1 ++ ) {
        bool tok = true ;
        for ( int pt2 = 0 ; pt2 < lnn[ j ] ; pt2 ++ ) {
          if ( buf[ pt1 + pt2 ] != q[ j ][ pt2 ] ) {
            tok = false ;
            break ;
          }
        }
        if ( tok ) {
          ok[ j ] ++ ;
          break ;
        }
      }
    }
  }
  for ( int i = 1 ; i <= m ; i ++ ) {
    printf( " %.5f" , (double)ok[ i ] / tot ) ;
  }
  puts( "" ) ;
}

int main() {
  srand( time( NULL ) ) ;
  int Cases;
  scanf( "%d" , &Cases ) ;
  for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
    init() ;
    printf( "Case #%d:" , cases ) ;
    process() ;
  }
  return 0 ;
}

