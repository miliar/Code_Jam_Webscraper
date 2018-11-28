//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;

int n ;
char s[ 20005 ] ;

void init() {
  scanf( "%s" , s ) ;
  n = strlen( s ) ;
}

vector< char > v ;

void process() {
  v.clear() ;
  int ans = 0 ;
  for ( int i = 0 ; i < n ; i ++ ) {
    if ( (int)v.size() == 0 ) {
      v.push_back( s[ i ] ) ;
    } else if ( v.back() == s[ i ] ) {
      ans += 10 ;
      v.pop_back() ;
    } else {
      v.push_back( s[ i ] ) ;
    }
  }
  ans += 5 * ( (int)v.size() / 2 ) ;
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

