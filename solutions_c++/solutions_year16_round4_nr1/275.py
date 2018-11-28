#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

string rec(int d, int cur) {
  if(d == 0) {
    if(cur == 0) return "P";
    if(cur == 1) return "R";
    if(cur == 2) return "S";
  }else{
    string c1 = rec(d - 1, cur);
    string c2 = rec(d - 1, (cur + 1) % 3);
    return min(c1 + c2, c2 + c1);
  }
}
int N;
int solve(int n, int P, int R, int S) {
  if(n == 0) {
    if(P) {
      cout << rec(N, 0) << endl;
    }
    if(R) {
      cout << rec(N, 1) << endl;
    }

    if(S) {
      cout << rec(N, 2)<<endl;
    }
    return 1;

  }
  assert((1 << n) == P + R + S);
  // pair of P,R
  int ret = 0;
  for(int i = 0; i <= min(P, R); i++) {
    int tp = P - i, tr = R - i;
    if(tp + tr == S) {
      ret |= solve(n - 1, i, tr, tp);
    }
  }
  return ret;
}
int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    cout << "Case #" << tc << ": ";
    int R, P, S;
    cin >> N >> R >> P >> S;
    if(!solve(N, P, R, S)) cout << "IMPOSSIBLE" << endl;
  }
}
