#include <set>
#include <iostream>
using namespace std;

bool foo(const multiset<int>& P, int reg, int spec) {
  int nspec = 0;
  for (auto i = P.rbegin(); i != P.rend(); i++) {
    nspec += (*i - 1) / reg;
  }
  return nspec <= spec;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    cin >> n;
    multiset<int> P;
    for (int i = 0; i < n; i++) {
      int p;
      cin >> p;
      P.insert(p);
    }

    int res = *P.rbegin();
    for (int s = 1; s < res - 1; s++) {
      int regl = 1, regr = res - s;
      while (regl < regr) {
        int regs = (regl + regr) / 2;
        if (foo(P, regs, s)) {
          regr = regs;
        } else {
          regl = regs + 1;
        }
      }
      res = min(res, regl + s);
    }
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}
