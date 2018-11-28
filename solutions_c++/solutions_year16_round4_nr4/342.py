#include <bits/stdc++.h>
using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using ll = long long;
using VL = vector<ll>;
using VVL = vector<VL>;
using P = pair<int, int>;
using VP = vector<P>;
using VVP = vector<VP>;

bool fail(int i, int n, VL &ms, ll mask) {
  if (i == n) return false;

  if ((ms[i] & mask) == 0) return true;
  for (int j = 0; j < n; ++j) {
    if (ms[i] & (1 << j)) {
      if (mask & (1 << j)) {
        if (fail(i + 1, n, ms, mask ^ (1 << j))) return true;
      }
    }
  }
  return false;
}

bool ok(int n, ll mask) {
  VL ms(n);
  for (int i = 0; i < n; ++i) {
    ms[i] = (mask >> (i * n)) & ((1 << n) - 1);
  }
  sort(ms.begin(), ms.end());
  do {
    if (fail(0, n, ms, (1 << n) - 1)) return false;
  } while (next_permutation(ms.begin(), ms.end()));
  return true;
}

void solve(int cas) {
  int n;
  cin >> n;
  ll mask = 0;
  VL ms(n);
  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    ms[i] = stoll(s.c_str(), nullptr, 2);
    mask |= (ms[i] << (n * i));
  }
  //cout << bitset<16>(mask) << endl;
  int best = n * n;
  for (int i = 0; i < (1 << (n * n)); ++i) {
    if ((i & mask) == mask) {
      int cost = __builtin_popcountll(mask ^ i);
      if (ok(n, i)) best = min(best, cost);
    }
  }
  cout << "Case #" << cas << ": " << best << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  for (int z = 1; z <= t; ++z) solve(z);
}
