#include<bits/stdc++.h>
using namespace std ;

int main() {
  freopen("D-small-attempt0.in","r",stdin) ;
  freopen("D-small-attempt0.out","w",stdout) ;
  int cases,caseno=1 ;
  cin >> cases ;
  while( cases -- ){
    int K , C , S ;
    cin >> K >> C >> S ;
    cout << "Case #" << caseno++ << ":" ;
    for( int i = 0 ; i < S ; i++ ){
      cout << " " << i+1 ;
    }cout << "\n" ;
  }
  return 0 ;
}

