#include <iostream>
using std::cin;
using std::cout;

#include <vector>
using std::vector;

#include <numeric>

bool seen_all(const vector<bool> &seen) {
  return std::accumulate(seen.begin(), seen.end(), true,
      [](bool x, bool y) { return x && y; } );
}

void check_digits(unsigned n, vector<bool> &seen) {
  while (n > 0) {
    seen[n % 10] = true;
    n /= 10;
  }
}

void solve() {
  unsigned N;
  cin >> N;
  if (N == 0) {
    cout << "INSOMNIA\n";
    return;
  }
  vector<bool> seen(10, false);
  unsigned n = 0;
  while (!seen_all(seen)) {
    n += N;
    check_digits(n, seen);
  }
  cout << n << '\n';
}

int main() {
  unsigned T;
  cin >> T;
  for (unsigned i = 0; i < T; ++i) {
    cout << "Case #" << (i+1) << ": ";
    solve();
  }
}
