#include <iostream>
#include <iterator>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cmath>
#include <limits>

using namespace std;

#define REP(n) for (int i = 0; i < (int) n; i++)
#define REPE(i, a, n) for (int i = a; i < (int) n; i++)
#define ALL(c) (c).begin(), (c).end()

const int MOD = 1000000007;
const double EPSILON = 1e-10;

inline void
gcjout(int t, int result) {
  cout << "Case #" << t << ": " << result << endl;
}

inline void
gcjout(int t, string result) {
  cout << "Case #" << t << ": " << result << endl;
}

int
main(int argc, char *argv[]) {
  int t;
  cin >> t;
  REPE(i, 1, t + 1) {
    unsigned long long x, r, c;
    cin >> x >> r >> c;
    bool result = false;
    switch (x) {
      case 4:
        if (r + c >= 7)
          result = true;
        break;
      case 3:
        if ((r == 3 && c > 1) || (c == 3 && r > 1))
          result = true;
        break;
      case 2:
        if ((r * c) % 2 == 0)
          result = true;
        break;
      default:
        result = true;
        break;
    }
    gcjout(i, (result ? "GABRIEL" : "RICHARD"));
  }
  return 0;
}