#include<bits/stdc++.h>
using namespace std ;

bool test( string s ){
  for( int i = 0 ; i < (int)s.size() ; i++ ){
    if( s[i] == '-' ) return true;
  }
  return false ;
}

int bfs(string s){
  map<string,bool>mp ;
  queue<pair<string,int>>Q;
  Q.push({s,0});
  mp[s]=1;
  while( !Q.empty() ){
    pair<string,int> u = Q.front() ;
    Q.pop() ;
    string t = u.first ;
    //cout <<t <<"\n" ;
    if( !test(t) )return u.second ;
    for( int i = 0 ; i < (int)t.size() ; i++ ) {
      if( t[i] == '-' ){
        t[i] = '+' ;
      }else {
        t[i] = '-' ;
      }
      if( mp.find(t)==mp.end() ) {
        mp[t]=1;
        Q.push({t,u.second+1}) ;
      }
    }
  }
}
int main(){
  freopen("B-large.in","r",stdin) ;
  freopen("B-large.out","w",stdout) ;
  int cases,caseno=1 ;
  cin >> cases ;
  while( cases -- ){
    string s,t ;
    cin >> s ;
    t = s ;
    int cnt = 0 ;
    while( test(s) ){
      cnt++ ;
      int idx = 0 ;
      if( s[idx] == '-' ){
        while(s[idx]=='-'){
          s[idx] = '+' ;
          idx++ ;
        }
      }else {
        while(s[idx]=='+'){
          s[idx] = '-' ;
          idx++ ;
        }
        while(s[idx]=='-'&& idx<(int)s.size()){
          s[idx] = '+' ;
          idx++ ;
        }
      }
    }
    //int ans = bfs(t) ;
    //assert(ans==cnt) ;
    cout << "Case #" << caseno++ << ": " << cnt << "\n" ;
  }
  return 0 ;
}
//#include<bits/stdc++.h>
//using namespace std ;
//
//int main(){
//  freopen("in.txt","w",stdout) ;
//  srand(time(NULL));
//  int n=1000;
//  cout << n << endl ;
//  for( int i = 0 ; i< n ; i++ ){
//    int q = rand()%17;
//    string s = "";
//    for( int i = 0 ; i < q ; i++ ){
//      if( rand()%2 == 0 ){
//        s +="+" ;
//      }else s +="-" ;
//    }
//    cout << s << "\n" ;
//  }
//  return 0 ;
//}
