#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

#define D(x) cout << #x << "=" << x << "\n"

int main(void) {
  int n_tests;
  cin >> n_tests;
  for (int test_case = 1; test_case <= n_tests; ++test_case) {
    int n, m;
    cin >> n >> m;
    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
      cin >> v[i];
    }
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    multiset<int, greater<int>> s;
    int n_discarded = 0;
    for (const auto& f: v) {
      if (!s.empty() && *s.begin() >= f) {
        n_discarded += 1;
        s.erase(s.begin());
      } else {
        s.insert(m - f);
      }
    }
    cout << "Case #" << test_case << ": " << n_discarded + s.size() << "\n";
  }
  return 0;
}

