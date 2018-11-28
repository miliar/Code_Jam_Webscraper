#include <algorithm>
#include <iostream>
#include <iomanip>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <cassert>
#include <set>

using namespace std;


const int MAXN = 37;
const int64_t mult = 36;

int64_t b, x[MAXN];

void Solve() {
  int n;
  cin >> b >> n;
  for (int i = 0; i < n; i++) {
    cin >> x[i];
  }

  for (int i = n; i < MAXN; i++) {
    x[i] = 0;
  }

  n = MAXN;

  sort(x, x + n);

  double best = 0;

  for (int i = 1; i <= n; i++) {
    int64_t remaining = b;
    int64_t cur = x[i - 1];
    int64_t used = 0;

    for (int j = 0; j < i; j++) {
      remaining -= cur - x[j];
      used += cur - x[j];
    }

    for (int j = i; j < n; j++) {
      remaining -= x[j] == cur ? 1 : 0;
    }

    if (remaining < 0) {
      continue;
    }

    int64_t used_part = 0;

    for (int j = i; j <= n; j++) {
      int64_t cap = j == n ? (1ll << 60) : x[j];
      int64_t delta = max(0ll, min(remaining / j, cap - 1 - cur));

      //used += delta * i;
      used_part += delta;
      remaining -= delta * j;
      cur += delta;

      best = max(best, ((double)(used * mult) / i) + ((used_part * mult) + (remaining - b)));
    }
  }

  cout << setprecision(10) << best << "\n";

}

int main() {
  int num_cases;
  cin >> num_cases;
  for (int i = 1; i <= num_cases; i++) {
    cout << "Case #" << i << ": ";
    Solve();
  }
}
