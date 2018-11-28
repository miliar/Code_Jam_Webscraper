#include<bits/stdc++.h>
using namespace std ;
void print(__int128 N){
  string s = "" ;
  while( N > 0 ){
    s+=((N%10)+'0') ;
    N/=10;
  }
  reverse(s.begin(),s.end()) ;
  cout << s << "\n" ;
}
int main(){
  freopen("A-large.in","r",stdin) ;
  freopen("A-large.out","w",stdout) ;
  int cases,caseno=1 ;
  cin >>cases ;
  while( cases -- ){
    map<int,int>mp ;
    int p ;
    cin >> p ;
    __int128 N = p ;
    __int128 t = N ;
    int cnt = 0 ;
    bool f = 0 ;
    while(1){
      __int128 p=N ;
      int l = mp.size() ;
      while( p > 0 ){
        int k = p%10 ;
        p/=10 ;
        mp[k]++ ;
      }
      if( mp.size() == 10 ){
        break ;
      }
      if( mp.size() == l )cnt++ ;
      else cnt = 0 ;
      if( cnt == 100 ){
        f = 1 ;
        break ;
      }
      N += t ;
    }
    if( f )cout << "Case #" << caseno++ << ": INSOMNIA\n" ;
    else {
      cout <<"Case #" << caseno++ << ": " ;
      print(N) ;
    }
  }
  return 0 ;
}
