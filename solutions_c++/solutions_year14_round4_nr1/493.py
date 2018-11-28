#include "stdio.h"
#include "algorithm"
#include "vector"

using namespace std;

const int MAX_N = 10010;

int main(){

  int t;
  scanf( "%d" , &t );

  for( int tc = 1; tc <= t; tc++ ){
    int n , x;
    scanf( "%d %d" , &n , &x );

    vector<int> a(n);

    for( int i = 0; i < n; i++ ){
      scanf( "%d" , &a[i] );
    }

    sort( a.begin() , a.end() );

    int ans = 0;
    vector<int>::iterator ite = a.begin();
    while( ite != a.end() ){
      ans++;
      vector<int>::iterator er = upper_bound( a.begin() , a.end() , x-(*ite) );
      if( er != a.begin() ) er--;
      //printf( "%d\n" , *er );
      if( er != ite ) a.erase( er );
      a.erase( ite );
    }

    printf( "Case #%d: %d\n" , tc , ans );
  }

  return 0;
}
