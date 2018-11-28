#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

int solve(int n) {
  int n0 = n;
  bitset<10> b;
  while (n) {
    for (int x = n; x; x /= 10) {
      b.set(x % 10);
    }
    if (b.all()) break;
    n += n0;
  }
  return n;
}

int main() {
  int T;
  cin >> T;
  forn(t, T) {
    int n;
    cin >> n;
    cout << "Case #" << t + 1 << ": ";
    int r = solve(n);
    if (!r)
      cout << "INSOMNIA\n";
    else
      cout << solve(n) << '\n';
  }
  return 0;
}
