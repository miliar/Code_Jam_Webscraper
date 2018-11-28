//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n , k ;
double p[ 300 ] ;

void init() {
  scanf( "%d%d" , &n , &k ) ;
  for ( int i = 1 ; i <= n ; i ++ ) scanf( "%lf" , &p[ i ] ) ;
  sort( p + 1 , p + n + 1 ) ;
}

double ans ;
double dp[ 205 ][ 205 ] ;
double t[ 300 ] ;

bool mtry( int l , int r ) {
  //for ( int i = 1 ; i <= k ; i ++ ) t[ i ] = p[ l + i - 1 ] ;

  dp[ 0 ][ 0 ] = 1 ;
  for ( int i = 1 ; i <= k ; i ++ ) {
    for ( int j = 0 ; j <= i ; j ++ ) {
      dp[ i ][ j ] = 0 ;
      if ( j < i ) dp[ i ][ j ] += ( 1.0 - t[ i ] ) * dp[ i - 1 ][ j ] ;
      if ( j > 0 ) dp[ i ][ j ] += t[ i ] * dp[ i - 1 ][ j - 1 ] ;
      //printf( "%d %d %.5f\n" , i , j , dp[ i ][ j ] ) ;
    }
  }
  if ( dp[ k ][ k / 2 ] > ans ) {
    ans = dp[ k ][ k / 2 ] ;
    return true ;
  } else return false ;
}

void process() {
  ans = 0 ;
  for ( int i = 0 ; i <= k ; i ++ ) {
    int id = 1 ;
    for ( int j = 1 ; j < 1 + i ; j ++ ) t[ id ++ ] = p[ j ] ;
    for ( int j = n - ( k - i ) + 1 ; j <= n ; j ++ ) t[ id ++ ] = p[ j ] ;
    mtry( 0 , 0 ) ;
  }
  //int bst = 0 ;
  //for ( int i = 0 ; i < ( 1 << n ) ; i ++ ) {
    //int id = 1 ;
    //for ( int j = 0 ; j < n ; j ++ ) {
      //if ( i & ( 1 << j ) ) t[ id ++ ] = p[ j + 1 ] ;
    //}
    //if ( id == k + 1 ) {
      //if ( mtry( 0 , 0 ) ) bst = i ;
    //}
  //}
  printf( "%.20f\n" , ans ) ;
  //for ( int j = 0 ; j < n ; j ++ ) {
    //if ( bst & ( 1 << j ) ) printf( "%.2f " , p[ j + 1 ] ) ;
  //} puts( "" ) ;
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

