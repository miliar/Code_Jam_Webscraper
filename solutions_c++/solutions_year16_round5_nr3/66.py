//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , s ;
struct pnt {
  int x , y , z ;
  int vx , vy , vz ;
  void mread() {
    scanf( "%d%d%d%d%d%d" , &x , &y , &z , &vx , &vy , &vz ) ;
  }
} p[ 1005 ] ;

struct edg {
  int x , y ;
  double dis ;
  edg( int _x , int _y , double _d ) : x( _x ) , y( _y ) , dis( _d ) {}
  bool operator<( const edg &a ) const {
    return dis < a.dis ;
  }
} ;

int pr[ 1005 ] ;
int grp ;
int fnd( int x ) {
  return ( pr[ x ] == x ) ? x : ( pr[ x ] = fnd( pr[ x ] ) ) ;
}
void mrg( int x , int y ) {
  int tx = fnd( x ) , ty = fnd( y ) ;
  if ( tx != ty ) {
    pr[ tx ] = ty ;
  }
}

vector< edg > ed ;

void init() {
  scanf( "%d%d" , &n , &s ) ;
  for ( int i = 0 ; i < n ; i ++ )
    p[ i ].mread() ;
  for ( int i = 0 ; i < n ; i ++ )
    pr[ i ] = i ;
  ed.clear() ;
  for ( int i = 0 ; i < n ; i ++ ) {
    for ( int j = i + 1 ; j < n ; j ++ ) {
      ed.emplace_back( i , j , (double)sqrt(
          (double)( p[ i ].x - p[ j ].x ) * ( p[ i ].x - p[ j ].x ) +
          (double)( p[ i ].y - p[ j ].y ) * ( p[ i ].y - p[ j ].y ) +
          (double)( p[ i ].z - p[ j ].z ) * ( p[ i ].z - p[ j ].z )
          ) ) ;
    }
  }
}

void process() {
  sort( ed.begin() , ed.end() ) ;
  for ( edg edge : ed ) {
    mrg( edge.x , edge.y ) ;
    if ( fnd( 0 ) == fnd( 1 ) ) {
      printf( "%.10f\n" , edge.dis ) ;
      return ;
    }
  }
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

