#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "B"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

const double eps = 1e-6;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n;
    cin >> n;
    double v, x;
    cin >> v >> x;
    vector<double> r(n), c(n);
    for (int i = 0; i < n; ++i) {
      cin >> r[i] >> c[i];
    }
    bool possible = true;
    double res;
    if (n == 1) {
      if (fabs(x - c[0]) > eps) {
        possible = false;
      } else {
        res = v / r[0];
      }
    } else if (n == 2) {
      if (fabs(c[0] - c[1]) > eps) {
        if (x < min(c[0], c[1]) - 1e-6 || x > max(c[0], c[1]) + 1e-6) {
          possible = false;
        } else {
          double v1 = v * (x - c[0]) / (c[1] - c[0]);
          double v0 = v - v1;        
          if (v0 < 1e-11) {
            v0 = 0;
          }
          if (v1 < 1e-11) {
            v1 = 0;
          }
          res = max(v0 / r[0], v1 / r[1]);
        }
      } else {
        if (fabs(x - c[0]) > eps) {
          possible = false;
        } else {
          res = v / (r[0] + r[1]);
        }
      }
    } else {
      res = 0;
    }
    cout << "Case #" << (test_index + 1) << ": ";
    if (!possible) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      printf("%.10lf\n", res);
    }
  }
  return 0;
}
