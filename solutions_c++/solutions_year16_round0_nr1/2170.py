#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

constexpr size_t kBuben = 1000000 + 100;

void solve() {
  ll n;
  cin >> n;
  vector<bool> used(10, false);
  for (ll i = 1; i <= kBuben; i++) {
    {
      ll x = n * i;
      if (x == 0)
        used[0] = true;
      else {
        while (x) {
          used[x % 10] = true;
          x /= 10;
        }
      }
    }
    bool ok = true;
    for (bool x : used)
      if (!x)
        ok = false;
    if (ok) {
      cout << (n * i) << endl;
      return;
    }
  }
  cout << "INSOMNIA" << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int ts;
  cin >> ts;

  for (int t = 1; t <= ts; t++) {
    cout << "Case #" << t << ": ";
    solve();
  }
  
  return 0;
}
