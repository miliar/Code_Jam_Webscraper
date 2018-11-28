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
    int n;
    cin >> n;
    cout << "Case #" << (test_index + 1) << ": ";
    cerr << "Case #" << (test_index + 1) << ": ";
    if (!n) {
      cout << "INSOMNIA" << endl;
      cerr << "INSOMNIA" << endl;
      continue;
    }
    vector<bool> was(10);
    int cnt_met = 0;
    ll x = n;
    while (cnt_met < 10) {
      ll y = x;
      while (y > 0) {
        if (!was[y % 10]) {
          ++cnt_met;
          was[y % 10] = true;
        }
        y /= 10;
      }
      if (cnt_met < 10) {
        x += n;
        if (x > ll(2000000000) * 1000000000) {
          cerr << "oops" << endl;
          abort();
        }
      }
    }
    cout << x << endl;
    cerr << x << endl;
  }
  return 0;
}
