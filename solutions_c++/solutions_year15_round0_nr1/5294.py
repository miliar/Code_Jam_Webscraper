#include <iostream>
#include <cstdio>
#include <string>

using namespace std ;

string str ; 

int t , n , sum , ans ;

int main(){
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> t ;
  for ( int l = 0 ; l < t ; l ++ ){
    cin >> n ;
    cin >> str ; 
    sum = 0 ; ans = 0 ;
    for ( int i = 0 ; i <= n ;i ++ ){
      sum += str[i] - '0';
      if( sum < i + 1 ) ans += i + 1 - sum , sum = i + 1 ;
    }
    printf("Case #%d: %d\n", l + 1 , ans);
  }
  return 0 ;
}
