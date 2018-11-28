#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int LL;

template <typename T>
LL bsearch(int n, LL N, LL p) {
  if (p == 1) return 0;
  if (p == N) return N-1;

  const T cmp;
  LL lo = 0, hi = N;
  while (hi-lo > 1) {
    LL m = (lo + hi) / 2;
    if (cmp(m, n, N, p))
      lo = m;
    else
      hi = m;
    }
  return lo;
  }

struct mustWin {
  bool operator()(LL z, int n, LL N, LL p) const {
    p -= 1; LL mask = 1LL << (n-1);

    while (mask) {
      if (p & mask) { // L
        if (!z) return true;
        N /= 2;
        z = (z-1) / 2;
        }
      else { // W
        if (z) return false;
        N /= 2;
        z = min(z, N-1);
        }
      mask >>= 1;
      }

    return true;
    }
  };

struct canWin {
  bool operator()(LL z, int n, LL N, LL p) const {
    p -= 1; LL mask = 1LL << (n-1);

    LL w = N-1-z;
    while (mask) {
      if (p & mask) { // L
        if (w) return true;
        N /= 2;
        w = min(w, N-1);
        }
      else { // W
        if (!w) return false;
        N /= 2;
        w = (w-1) / 2;
        }
      mask >>= 1;
      }

    return true;
    }
  };

int main() {
  int nc; cin >> nc;
  for (int curC = 1; curC <= nc; ++curC) {
    int n; cin >> n;
    LL N = 1LL << n, p; cin >> p;

    LL y = bsearch<mustWin>(n, N, p);
    LL z = bsearch<canWin>(n, N, p);

    cout << "Case #" << curC << ": " << y << ' ' << z << '\n';
    }
  }

