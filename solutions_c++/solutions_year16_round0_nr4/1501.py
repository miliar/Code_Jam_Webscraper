#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;

u64 getNth(u64 K, u64 C, u64 n) {
  if (C==1) {
    return n;
  }
  u64 ans=1;
  for (u64 i=1; i<C; i++) {
    ans *= K;
  }
  return ans*n + getNth(K, C-1, n);
}

int main() {
  u64 K, C, S;
  int T;
  cin >> T;
  for (int t=1; t<=T;t++) {
    cin >> K >> C >> S;
    cout << "Case #" << t << ":";
    if (S < K) {
      cout << " IMPOSSIBLE" << endl; //not quite correct :P
    } else {
      if (K==1) {
        cout << " 1" << endl;
      } else {
        for(u64 i=0; i<S; i++) {
          cout << " " << getNth(K,C,i)+1;
        }
        cout << endl;
      }
    }
  }
}
