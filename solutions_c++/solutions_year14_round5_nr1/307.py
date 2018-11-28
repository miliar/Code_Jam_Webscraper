#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iomanip>

using namespace std;

const int N_MAX = 1000008;
int N;
long long counts[N_MAX];

long long range_count(int lower, int upper) {
  if (upper < lower)
    return 0LL;
  return counts[upper] - counts[lower];
}

long long cost(int a, int b) {
  return max(max(range_count(0, a),
                 range_count(a, b + 1)),
             range_count(b + 1, N));
}

void init() {
  long long p, q, r, s;
  cin >> N >> p >> q >> r >> s;

  counts[0] = 0;
  for (long long i = 0; i < N; i++) {
    long long amt = ((i * p + q) % r) + s;
    assert(amt > 0);
    counts[i + 1] = counts[i] + amt;
  }
}

void solve_case(int t) {
  init();

  // for (int i = 0; i <= N; i++) {
  //   cout << counts[i] << " ";
  // }
  // cout << endl;

  long long tot = counts[N];
  long long min_cost = tot;
  int a = 0;
  for (int b = 0; b < N; b++) {
    while (a < b && cost(a + 1, b) < cost(a, b))
      a++;
    //    cout << "a " << a << " b " << b << endl;

    min_cost = min(min_cost, cost(a, b));
  }

  double prob = 1.0 - ((double) min_cost) / ((double) tot);
  cout << "Case #" << t << ": ";
  cout << fixed << setprecision(9) << prob << '\n';
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
