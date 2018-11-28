#include<iostream>
#include<stdio.h>
#include<string>

using namespace std ;

int main(){
  int t ;
  cin >> t ;
  int ans ;
  int smax,cur, count;
  string p ;

  p.clear() ;

  for(int i=1;i<=t;i++){
    ans = smax = cur = count = 0 ;
    cin >> smax >> p ;
    for(int j=0;j<p.length();j++){
      cur = p[j]-'0' ;
      if(cur){
        if(j > count){
          ans += j - count ;
          count = j ;
        }
      }

      count = count + cur ;

    }

    cout << "Case #" << i << ": " << ans << endl ;

  }

  return 0 ;
}
