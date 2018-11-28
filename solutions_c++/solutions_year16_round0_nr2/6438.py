#include <bits/stdc++.h>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int test = 1; test <= t; test++){
    string pStack;
    cin >> pStack;
    int flips = 0;
    for(int i = pStack.size()-1; i > -1; i--){
      if(pStack[i] == '-'){
        for(int j = i; j > -1; j--){
          if(pStack[j] == '-')
            pStack[j] = '+';
          else
            pStack[j] = '-';
        }
        flips++;
      }
    }
    cout << "Case #" << test << ": " << flips << endl;
  }
}