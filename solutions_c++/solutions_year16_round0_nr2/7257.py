#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int T;
string S;

bool check(){
  for(int i=0;i<(int)S.size();i++) if( S[i] == '-' ) return true;
  return false;
}

void rev(){
  char c = S[0];
  for(int i=0;i<(int)S.size();i++){
    if( S[i] != c ){
      for(int j=0;j<i;j++) S[j] = S[i];
      return;
    }    
  }
  for(int i=0;i<(int)S.size();i++) S[i] = '+';
}

int main(){
  cin >>T;  
  for(int ttt=1;ttt<=T;ttt++){
    cin >> S;
    int res=0;
    while( check() ) {
      res++;
      rev();
    }    
    cout << "Case #" << ttt << ": ";
    cout << res << endl;
  }
}
