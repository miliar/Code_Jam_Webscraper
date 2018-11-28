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
#define PROBLEM_ID "pancake_flipper"

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
    string pancakes;
    int k;
    cin >> pancakes >> k;
    int res = 0;
    for (int pos = 0; pos + k <= pancakes.length(); ++pos) {
      if (pancakes[pos] == '-') {
        ++res;
        for (int i = pos; i < pos + k; ++i) {
          if (pancakes[i] == '-') {
            pancakes[i] = '+';
          }
          else {
            pancakes[i] = '-';
          }
        }
      }
    }
    if (pancakes != string(pancakes.length(), '+')) {
      cout << "Case #" << (test_index + 1) << ": " << "IMPOSSIBLE" << endl;
      cerr << "Case #" << (test_index + 1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }
    cout << "Case #" << (test_index + 1) << ": " << res << endl;
    cerr << "Case #" << (test_index + 1) << ": " << res << endl;
    
    
  }
  return 0;
}
