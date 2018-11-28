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

int
main(int argc, char *argv[]) {
  int t;
  cin >> t;
  REPE(i, 1, t + 1) {
    int shyness_max;
    int ovation_cur = 0;
    int needed_friend = 0;
    cin >> shyness_max;
    REPE(level, 0, shyness_max + 1) {
      char ch;
      cin >> ch;
      int num = ch - '0';
      if (ovation_cur < level) {
        needed_friend += level - ovation_cur;
        ovation_cur += level - ovation_cur;
      }
      ovation_cur += num;
    }
    cout << "Case #" << i << ": " << needed_friend << endl;
  }
  return 0;
}