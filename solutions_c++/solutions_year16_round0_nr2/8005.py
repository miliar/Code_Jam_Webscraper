#include <iostream>

using namespace std;

int solve() {
  char S[128];
  int f = 0;
  cin >> S;
  char c = S[0];

  for(int i=0;;i++) {
    if(!S[i]) break;
    if(c != S[i]) {
      f++;
      c = S[i];
    }
  }

  if(c=='-') f++;
  return f;
}

int main() {
  int T;
  cin >> T;

  for(int i=1;i<=T;i++) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
