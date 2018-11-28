#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int digits [10];

void reset(){
  for(int i = 0; i < 10; ++i) digits[i] = 0;
}

void countD(ll n){
  while(n){
    int d = n%10;
    ++digits[d];
    n /= 10;
  }
}
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC; cin >> TC;
  for(int i = 1; i <= TC; ++i){
  	reset();
    int n; cin >> n;
    int move = n;
    int counter = 0;
    bool done = false;
    while(n && !done){
      done = true;
      move = n * ++counter;
      countD(move);
      for(auto &a: digits){
        if(!a){
          done = false;
          break;
        }
      }
    }
    cout << "Case #" << i << ": ";
    if(!done) cout << "INSOMNIA";
    else cout << move;
    cout << "\n";
  }
}
