#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <cstdlib>

using namespace std ; 

typedef long long int64; 

void open_file(){
    string s = "3.txt" ; 
    freopen(s.c_str(),"r", stdin); 
    freopen( (s + "out.txt").c_str(), "w", stdout); 
}

vector< int64 > table ;  

bool is (int64 x ){
    string res = "" ;
    for( ; x ; x/=10){
        res = res + (char)( x % 10 +'0') ; 
    }
    string  t = res; reverse(res.begin(), res.end()) ; 
    return t == res; 
}

void init (){
    for(int i=1; i <= 10000000LL ; ++i){ 
        if( is(i) && is ( 1LL*i*i)){ 
            table.push_back(1LL*i*i) ;
        }
    }
}

int64 gao( int64 x ){ 
    return upper_bound( table.begin(), table.end(), x ) - table.begin() ; 
}

int main (){ 
  open_file () ; 
  init () ; 
  int T ; cin >> T ;
  for(int Cas = 1 ; Cas <= T ; ++Cas){ 
      int A, B ; 
      cin >> A >> B ; 
      cout <<"Case #"<<Cas<<": "<< gao(B)-gao(A-1)<< endl ;
  }
  return 0; 
}


