#include<bits/stdc++.h>
using namespace std;

int T, K;
string S;

int main(){
  cin >> T;
  for(int t=1; t<=T; t++){
    cin >> S;
    cin >> K;
    int flipN = 0;
    for(int i=0; i<=S.length()-K; i++){
      if(S[i] == '-'){
        for(int j=i; j<i+K; j++){
          if(S[j] == '-')
            S[j] = '+';
          else
            S[j] = '-';
        }
        flipN++;
      }
      //cout << S << endl;
    }
    bool klappt = true;
    for(int i=0; i<S.length(); i++){
      if(S[i] == '-'){
        klappt = false;
      }
    }
    cout << "Case #" << t << ": ";
    if(klappt)
      cout << flipN << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }

}
