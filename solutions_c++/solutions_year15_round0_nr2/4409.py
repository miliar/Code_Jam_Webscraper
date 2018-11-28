#include <iostream>
#include <cstdio>
#include <string>

using namespace std ;

string str ; 

int t , n , a[100] , ans ;

void rec( int spec , int mx, int i){
  if( i == n ){
    if( mx + spec < ans ) ans = mx + spec ;
    return ;
  } 
  for( int r = 1 ; r < 4 ; r ++ ){
    int x = a[i] /r ;
    if( a[i]%r ) x ++ ;
    x = max( x , mx) ;
    rec( spec + r - 1, x , i + 1 ) ;
  }
}

int main(){
   freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);
  cin >> t ;
  for ( int l = 0 ; l < t ; l ++ ){
    cin >> n ;
    ans = 100000;
    for ( int i = 0 ; i < n ;i ++ ){
      cin >> a[i] ;
    }
    rec(0 , 0 , 0  ) ;
    printf("Case #%d: %d\n", l + 1 , ans);
  }
  return 0 ;
}
