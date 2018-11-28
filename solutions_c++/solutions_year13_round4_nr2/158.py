#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int64;

int64 calcbestpos(int64 N, int64 team) {
  if (team == 0) {
    return 1;
  }

  int64 T = 1LL << N;
  int64 cmp = 0;
  for (int64 i=0; i<N; ++i) {
    cmp += T>>(i+1);
    if (team <= cmp) {
      return 1LL << (i+1);
    }
  }
  assert(false);
}

int64 calcworstpos(int64 N, int64 team) {
  if (team == 0) {
    return 1;
  }

  for (int64 k=N; k>=0; --k) {
    if (team >= (1LL<<k) - 1) {
      // Can lose k games
      int64 out = 1;
      for (int i=0; i<k; ++i) {
        out += 1LL << (N-i-1);
      }
      return out;
    }
  }
  assert(false);
}

template<typename F>
int64 bs(int64 N, int64 P, F f) {
  int64 lo = 0, hi = (1LL<<N) - 1;
  while (lo < hi) {
    int64 mid = (lo + hi + 1) / 2;
    if (f(N, mid) <= P) {
      lo = mid;
    } else {
      hi = mid - 1;
    }
  }
  return lo;
}

int main() {
  cin.sync_with_stdio(0);

  int64 T;
  cin >> T;
  for (int64 tt=1; tt<=T; ++tt) {
    int64 N, P;
    cin >> N >> P;
    cout << "Case #" << tt << ": " << bs(N, P, calcworstpos) << ' ' << bs(N, P, calcbestpos) << '\n';
  }
  
  return 0;
}
