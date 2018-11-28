#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = __int128;

constexpr ll kBuben = 10000;

inline bool check_bit(uint64_t mask, uint64_t bit) {
  return ((mask >> bit) & 1) != 0;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  constexpr int N = 32;
  constexpr int J = 500;
  set<uint64_t> founded;

  cout << "Case #1:" << endl;

  while (founded.size() < J) {
    uint64_t mask = 0;
    for (int i = 0; i < N; i++) {
      mask <<= 1;
      mask |= (rand() & 1);
    }
    if (!check_bit(mask, 0) || !check_bit(mask, N - 1))
      continue;
    if (founded.count(mask))
      continue;
    bool bad = false;
    vector<ll> factors;
    for (int base = 2; base <= 10 && !bad; base++) {
      ll number = 0;
      for (int i = 0; i < N; i++) {
        ll bit = check_bit(mask, i);
        number *= base;
        number += bit;
      }
      bool found = false;
      for (ll i = 2; i * i <= number && !found && i <= kBuben; i++) {
        if (number % i == 0) {
          factors.pb(i);
          found = true;
        }
      }
      if (!found)
        bad = true;
    }
    if (!bad) {
      founded.insert(mask);
      assert(factors.size() == 9);
      for (int i = 0; i < N; i++) {
        cout << check_bit(mask, i);
      }
      for (ll factor : factors) {
        cout << " " << int64_t(factor);
      }
      cout << endl;
    }
  }


  
  return 0;
}
