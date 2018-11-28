#include <bits/stdc++.h>
using namespace std;

int x,r,c;

bool solve(){
  if(x == 1) return true;
  else if(x == 2 && (r % 2 == 0 || c % 2 == 0)) return true;
  else if(x == 3 && (r == 3 && c >= 2 || r >= 2 && c == 3)) return true;
  else if(x == 4 && (r >= 3 && c == 4 || r == 4 && c >= 3)) return true;
  else return false;
}

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> x >> r >> c;
    cout << "Case #" << t << ": " << (solve() ? "GABRIEL" : "RICHARD") << endl;
  }
}
