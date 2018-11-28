//by tzupengwang™
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int k , n ;
char s[ 1005 ] ;

void init() {
  scanf( "%s%d" , s , &k ) ;
  n = strlen( s ) ;
}

void process() {
  int ans = 0 ;
  for ( int i = 0 ; i + k <= n ; i ++ ) {
    if ( s[ i ] == '-' ) {
      ans ++ ;
      for ( int j = i ; j < i + k ; j ++ ) {
        if ( s[ j ] == '-' ) s[ j ] = '+' ;
        else s[ j ] = '-' ;
      }
    }
  }
  bool ok = true ;
  for ( int i = 0 ; i < n ; i ++ ) if ( s[ i ] == '-' )
    ok = false ;
  if ( ok ) printf( "%d\n" , ans ) ;
  else puts( "IMPOSSIBLE" ) ;
}

int main() {
/*
#ifdef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
#endif
*/
  int Cases;
  scanf( "%d" , &Cases ) ;
  for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
    init() ;
    printf( "Case #%d: " , cases ) ;
    process() ;
  }
/*
*/
  return 0 ;
}

