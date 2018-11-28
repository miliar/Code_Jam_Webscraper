#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
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

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

#define PROBLEM_ID "B"

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    ll n, p;
    cin >> n >> p;
    ll sum = 1;
    int best_k = 0;
    while (best_k < n && sum + (ll(1) << (n - (best_k + 1))) <= p) {
      sum += (ll(1) << (n - (best_k + 1)));
      ++best_k;
    }
    ll a = (ll(1) << (best_k + 1)) - 2;
    if (best_k == n) {
      a = (ll(1) << n) - 1;
    }
    best_k = 0;
    while ((ll(1) << (best_k + 1)) <= p) {
      ++best_k;
    }
    ll b = (ll(1) << n) - (ll(1) << (n - best_k));
    cout << "Case #" << test_index + 1 << ": " << a << ' ' << b << endl;
    cerr << "Case #" << test_index + 1 << ": " << a << ' ' << b << endl;
  }
  return 0;
}
