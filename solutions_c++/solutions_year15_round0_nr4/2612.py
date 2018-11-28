#include <bits/stdc++.h>

using namespace std;

int main(){
  int Tc;
  const string names[2] = {"RICHARD","GABRIEL"};
  cin >> Tc;
  for(int T = 0 ; T < Tc ; T++){
    int X,R,C,idx = -1;
    cin >> X >> R >> C;
    int rem = R*C-X;
    if(X == 1){
      idx = 1;
    }else if(X == 2){
      if(rem%2){
	idx = 0;
      }else{
	idx = 1;
      }
    }else if(X == 3){
      if(rem%3 || rem == 0){
	idx = 0;
      }else{
	idx = 1;
      }
    }else{
      if(rem%4 || rem == 0 || rem == 4){
	idx = 0;
      }else{
	idx = 1;
      }
    }
    cout << "Case #" << T+1 << ": " << names[idx] << endl;  
  }
  return 0;
}
