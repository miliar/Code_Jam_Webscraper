#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    set<int> s = {0,1,2,3,4,5,6,7,8,9};
    ll N; cin >> N;
    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", t);
      continue;
    }
    for (int i = 1; i <= 100; ++i) {
      ll temp = i*N;
      while (temp > 0) {
        int digit = temp % 10;
        temp /= 10;
        s.erase(digit);
      }
      if (s.empty()) {
        printf("Case #%d: %lld\n", t, i*N);
        break;
      }
    }
    if (!s.empty()) {
      printf("Case #%d: POOP\n", t);
      return 0;
    }
  }
  return 0;
}