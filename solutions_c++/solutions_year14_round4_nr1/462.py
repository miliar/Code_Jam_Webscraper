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
    int n, X;
    cin >> n >> X;
    vi a(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    multiset<int> s(a.begin(), a.end());
    int result = 0;
    while (!s.empty()) {
      ++result;
      int biggest = *s.rbegin();
      s.erase(s.find(biggest));
      multiset<int>::iterator it = s.upper_bound(X - biggest);
      if (it == s.begin()) {        
        continue;
      }
      --it;
      s.erase(it);
    }
    cout << "Case #" << (test_index + 1) << ": " << result << endl;
  }
  return 0;
}
