#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;

ll N, p, q, r, s;
ll A[1000000];
ll ps[1000000];

void read()
{
  cin >> N >> p >> q >> r >> s;
  for (int i = 0; i < N; i++) {
    A[i] = ((i * p) % r + q) % r + s;
  }
}

void solve()
{
  read();
  
  ps[0] = A[0];
  for (int i = 1; i < N; i++) {
    ps[i] = A[i] + ps[i-1];
  }

  ll total = ps[N-1];

  // 2 partitions
  ll best = total;
  for (int i = 0; i < N; i++) {
    ll part1 = ps[i];
    ll part2 = total - ps[i];
    ll t = max(part1, part2);
    best = min(best, t);
  }

  // 3 partitions
  for (int i = N-1; i > 0; i--) {
    ll part3 = total - ps[i-1];
    ll first = ps[i-1];
    int t = lower_bound(ps, ps+i, first/2) - ps;
    ll part1, part2;
    if (t) {
      part1 = ps[t-1];
      part2 = first - part1;
      best = min(best, max(max(part1, part2), part3));
    }
    if (t+1 < i) {
      part1 = ps[t];
      part2 = first - part1;
      best = min(best, max(max(part1, part2), part3));
    }
    if (t-1 > 0) {
      part1 = ps[t-2];
      part2 = first - part1;
      best = min(best, max(max(part1, part2), part3));
    }
  }
  cout << fixed << setprecision(12) << 1 - (long double)best / total << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
