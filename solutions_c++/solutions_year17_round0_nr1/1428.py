#ifdef __GNUC__

#include <bits/stdc++.h>
using namespace std;

// #include <bits/extc++.h>
// using namespace __gnu_cxx;
// using namespace __gnu_pbds;

#include <ext/rope>
#include <ext/algorithm>
#include <ext/numeric>
using namespace __gnu_cxx;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/trie_policy.hpp>
using namespace __gnu_pbds;

#endif

#include <cmath>
#include <limits>
#include <utility>
#include <vector>
using namespace std;

#define endl '\n'
#define X first
#define Y second
#define A first
#define B second
#define U first
#define V second
#define fi first
#define se second
#define ALL(C) std::begin(C), std::end(C)

using LL = long long;
using Pii = std::pair<int, int>;
using Vi = std::vector<int>;
using VVi = std::vector<Vi>;

constexpr auto eps = 1.0e-9;
const auto pi = std::acos(-1.0);
const auto e = std::exp(1.0);
const auto phi = (1.0 + std::sqrt(5.0)) / 2.0;

constexpr auto k7 = 1000 * 1000 * 1000 + 7;
constexpr auto k9 = 1000 * 1000 * 1000 + 9;
constexpr auto inf = std::numeric_limits<int>::max();



int main(int argc, char* argv[]) {
#ifndef ONLINE_JUDGE
  if (argc > 1) freopen(argv[1], "rt", stdin);
  if (argc > 2) freopen(argv[2], "wt", stdout);
#endif  // ONLINE_JUDGE
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.setf(ios::fixed);
  cout.precision(6);

  int t;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    string s;
    cin >> s;
    int k;
    cin >> k;
    string newline;
    getline(cin, newline);
    int c = 0;
    for (int j = 0; j <= s.size() - k; ++j) {
      if (s[j] == '-') {
        ++c;
        for (int dj = 0; dj < k; ++dj) {
          s[j+dj] = (s[j+dj] == '-' ? '+' : '-');
        }
      }
    }
    bool f = true;
    for (int j = max((int)s.size() - k + 1, 0); j < s.size(); ++j) {
      if (s[j] == '-') {
        f = false;
      }
    }
    if (f) {
      cout << c << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
