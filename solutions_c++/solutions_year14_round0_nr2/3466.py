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
    double c, f, x;
    cin >> c >> f >> x;
    const int MAX_FARMS = 100000;
    double speed = 2.0;
    double best = 1e100;
    double spent = 0;
    for (int farms = 0; farms < MAX_FARMS; ++farms) {
      double cur = spent + x / speed;
      best = min(best, cur);
      spent += c / speed;
      speed += f;
    }
    cout << "Case #" << (test_index + 1) << ": ";
    printf("%.10lf\n", best);
  }
  return 0;
}
