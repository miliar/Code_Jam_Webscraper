#include <iostream>
#include <math.h>
using namespace std;

int main (){
  int T, S, K, C;
  cin >> T;
  for (int ct = 1; ct <= T; ++ct){
    cin >> K >> C >> S;
    if ((S < K/C) || (S == K/C && K%C != 0)){
      cout << "Case #" << ct << ": " << "IMPOSSIBLE" << endl;
    }
    if (S == K){
      cout << "Case #" << ct << ": "; 
      for (int s = 1; s <= S; ++s){
        cout << s << ' ';
      }
      cout << endl;
    }
    /*else{
      cout << "Case #" << ct << ": "; 
      for (int s = 0; s < K/C; ++s){
        int pos = 0;
        for (int i = 0; i < C; ++i){
          pos = pos + (s*C+i)*pow(K,C-1-i);
        }
        pos++;
        cout << pos << ' ';
      }
      if(K%C != 0){
        int s = (K/C)*C;
        int pos = 0;
        for (int i = 0; i < K%C; ++i){
          pos = pos + (s+i)*pow(K,C-1-i);
        }
        pos++;
        cout << pos << ' ';
      }
      cout << endl;
    }*/
  }


}
