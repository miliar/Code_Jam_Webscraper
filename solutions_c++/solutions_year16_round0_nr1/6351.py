#include <bits/stdc++.h>

using namespace std;

bool seen[11];

void seenDigits(int n){
  while(n>0){
    seen[n%10] = true;
    n /= 10;
  }
}

bool seenAll(){
  bool s = true;
  for(int i = 0; i < 10; i++){
    s &= seen[i];
  }
  return s;
}

int main(){
  int t, n;
  cin >> t;
  for(int test = 1; test <= t; test++){
    cout << "Case #" << test << ": "; 
    for(int i = 0; i < 10; i++)
      seen[i] = false;
    cin >> n;
    for(int i = 1; i < 100; i++){
      seenDigits(i*n);
      if(seenAll()){
        cout << i*n << endl;
        break;
      }
    }
    if(!seenAll()){
      cout << "INSOMNIA\n";
    }
  }
}