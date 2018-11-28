#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include <vector>
#include <math.h>

using namespace std;

int backtrack(multiset<int>& ps) {
  auto last = prev(ps.end());
  int max = *last;
  ps.erase(last);
  int result = max;
  for (int i = 2; i <= sqrt(max); i++) {
    int a = max / i;
    int b = max - a;
    ps.insert(a);
    ps.insert(b);
    result = min(result, backtrack(ps) + 1);
    ps.erase(ps.find(b));
    ps.erase(ps.find(a));
  }
  ps.insert(max);
  return result;
}

void run(int t) {
  int D; cin >> D;
  multiset<int> ps;
  for (int i = 0; i < D; i++) {
    int p; cin >> p;
    ps.insert(p);
  }
  cout << "Case #" << t << ": " << backtrack(ps) << endl;
}

int main() {
  cout << setprecision(7) << fixed;
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    run(t);
  }
}
