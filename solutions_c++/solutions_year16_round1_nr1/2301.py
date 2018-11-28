#include<bits/stdc++.h>
using namespace std;
string S;
int T;
int main(){
  cin>> T;
  for(int ttt=1;ttt<=T;ttt++){
    cin >> S;
    string res = "";
    res += S[0];
    for(int i=1;i<(int)S.size();i++){
      if( S[i] >= res[0] ){
        res = S[i] + res;
      } else
        res += S[i];
    }
    cout << "Case #" << ttt << ": ";
    cout << res << endl;
  }
}
