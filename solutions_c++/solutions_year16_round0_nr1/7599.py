#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int T,N;

void solve(int k){
  map<int,int> M;
  int digits[10] = {};
  int i, remainingDigits = 10;
  long long x = N;
  for(i=0;i<1000 && remainingDigits;i++){
    long long a = x;
    while(a){
      if(!digits[a%10]){
        digits[a%10] = 1;
        remainingDigits--;
      }
      a /= 10;
    }
    x += N;
  }
  cout << "Case #" << k << ": ";
  if(remainingDigits)
    cout << "INSOMNIA" << endl;
  else
    cout << x-N << endl;
}

int main(){
  cin >> T;
  for(int i=1;i<=T;i++){
    cin >> N;
    solve(i);
  }
  return 0;
}
