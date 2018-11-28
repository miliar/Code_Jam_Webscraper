#include <iostream>
#include <vector>
using namespace std;

#ifndef MAXP
#define MAXP 1000
#endif

typedef vector<int> vi;

int main() {
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int D; cin >> D;
    vi P(D); for (int& x : P) cin >> x;
    if (cas == 33) cerr << D << endl;
    int res = MAXP;
    for (int m = 1; m <= MAXP; ++m) {
      int r = m;
      for (int x : P) r += (x-1)/m;
      res = min(res, r);
    }
    cout << "Case #" << cas << ": " << res << endl;
  }
}