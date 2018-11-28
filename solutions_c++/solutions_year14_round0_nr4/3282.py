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
#define PROBLEM_ID "D"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n;
    cin >> n;
    vector<double> naomi(n);
    for (int i = 0; i < n; ++i) {
      cin >> naomi[i];
    }
    vector<double> ken(n);
    for (int i = 0; i < n; ++i) {
      cin >> ken[i];
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int ans1 = 0;
    for (int i = 0; i < n; ++i) {
      if (naomi[i] > ken[ans1]) {
        ++ans1;
      }
    }
    int ans2 = n;
    vb used(n, false);
    for (int ki = n - 1; ki >= 0; --ki) {
      int lastni = -1;
      for (int ni = n - 1; ni >= 0; --ni) {
        if (!used[ni] && naomi[ni] < ken[ki]) {
          lastni = ni;
          break;
        }
      }
      if (lastni == -1) {
        break;
      }
      int bestki = -1;
      for (int ki2 = n - 1; ki2 >= 0; --ki2) {
        if (ken[ki2] < naomi[lastni]) {
          bestki = ki2;
          break;
        }
      }
      if (bestki == -1) {
        for (int ni = 0; ni < n; ++ni) {
          if (!used[ni]) {
            used[ni] = true;
            --ans2;
            break;
          }
        }
        continue;
      }
      int bestni = -1;
      for (int ni = lastni; ni >= 0; --ni) {
        if (!used[ni] && naomi[ni] < ken[ki] && naomi[ni] > ken[bestki]) {
          bestni = ni;
        }
      }
      if (bestni != -1) {
        used[bestni] = true;
        ans2--;
      } else {
        abort();
      }
    }
    if (ans2 > ans1) {
      cerr << ans1 << ' ' << ans2 << endl;
      abort();
    }
    cout << "Case #" << (test_index + 1) << ": ";
    cout << ans1 << ' ' << ans2 << endl;
  }
  return 0;
}
