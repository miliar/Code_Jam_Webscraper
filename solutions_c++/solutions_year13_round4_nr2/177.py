#include <iostream>
using namespace std;

long long worst_rank(long long n, long long x) {
  if (n == 0 || x == 0) return 0;
  return (1LL<<(n-1)) + worst_rank(n-1, (x-1)/2);
}

long long will_win(long long n, long long p) {
  long long low = 0, hi = (1LL << n);
  while (hi - low > 1) {
    long long mid = (low + hi) / 2;
    if (worst_rank(n, mid) >= p) hi = mid;
    else low = mid;
  }
  return low;
}

long long best_rank(long long n, long long x) {
  if (n == 0) return 0;
  if (x == (1LL << n)-1) return x;
  return best_rank(n-1, (x+1)/2);
}

long long can_win(long long n, long long p) {
  long long low = 0, hi = (1LL << n);
  while (hi - low > 1) {
    long long mid = (low + hi) / 2;
    if (best_rank(n, mid) >= p) hi = mid;
    else low = mid;
  }
  return low;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    long long n, p; cin >> n >> p;
    cout << "Case #" << c << ": " << will_win(n, p) << " " << can_win(n, p) << endl;
  }
  return 0;
}
