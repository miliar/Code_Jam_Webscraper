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
#define PROBLEM_ID "A"

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

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int r, c;
    cin >> r >> c;
    vector<string> field(r);
    for (int i = 0; i < r; ++i) {
      cin >> field[i];
    }
    bool possible = true;
    int res = 0;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (field[i][j] == '.') {
          continue;
        }
        bool ok = false;
        bool same = false;
        if (i > 0) {
          for (int k = 0; k < i; ++k) {
            if (field[k][j] != '.') {
              ok = true;
              if (field[i][j] == '^') {
                same = true;
              }
            }
          }
        }
        if (j > 0) {
          for (int k = 0; k < j; ++k) {
            if (field[i][k] != '.') {
              ok = true;
              if (field[i][j] == '<') {
                same = true;
              }
            }
          }
        }
        if (i + 1 < r) {
          for (int k = i + 1; k < r; ++k) {
            if (field[k][j] != '.') {
              ok = true;
              if (field[i][j] == 'v') {
                same = true;
              }
            }
          }
        }
        if (j + 1 < c) {
          for (int k = j + 1; k < c; ++k) {
            if (field[i][k] != '.') {
              ok = true;
              if (field[i][j] == '>') {
                same = true;
              }
            }
          }
        }
        if (!ok) {
          possible = false;
          break;
        }
        if (!same) {
          ++res;
        }
      }
      if (!possible) {
        break;
      }
    }
    cout << "Case #" << (test_index + 1) << ": ";
    if (!possible) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << res << endl;
    }
  }
  return 0;
}
