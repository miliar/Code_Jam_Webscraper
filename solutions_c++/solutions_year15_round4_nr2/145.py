#define NDEBUG
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

#define repeat(n) for (int repc = (n); repc > 0; --repc)
int fcmpl( const long double &a, const long double &b, const long double EPS = 1e-9 ) {
   if ( fabsl( a-b ) < EPS ) return 0;
   else if ( a < b ) return -1;
   else return 1;
}
#define ALL(x) (x).begin(), (x).end()

struct Pipa {
  long double R, C;
};

template<typename Iter>
long double takewhile(Iter begin, Iter end, long double target_volume, long double max_time) {
  long double num = 0, denom = 0;
  for (auto it = begin; target_volume > 0 && it != end; ++it) {
    long double t = min(max_time, target_volume / it->R);
    long double v = t * it->R;
    target_volume -= v;
    num += v * it->C;
    denom += v;
  }
  return num / denom;
}

bool can(long double V, long double T, const vector<Pipa> &pipe, long double max_time) {
  long double minT = takewhile(pipe.begin(), pipe.end(), V, max_time);
  long double maxT = takewhile(pipe.rbegin(), pipe.rend(), V, max_time);
  return fcmpl(minT, T, 1e-12) <= 0 && fcmpl(T, maxT, 1e-12) <= 0;
}

void solve() {
  int N;
  long double V, X;
  cin >> N >> V >> X;
  vector<Pipa> pipe(N);
  long double rsum = 0;
  for (Pipa& p : pipe) {
    cin >> p.R >> p.C;
    rsum += p.R;
  }
  sort(ALL(pipe), [](Pipa p1, Pipa p2) { return p1.C < p2.C; });
  long double lo = V / rsum, hi = 1e18;
  repeat (1000) {
    long double mid = (lo + hi) / 2;
    if (can(V, X, pipe, mid)) {
      hi = mid;
    } else {
      lo = mid;
    }
  }
  if (lo > 1e10) {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%.9Lf\n", lo);
  }
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: ", tt);
    solve();
    fflush(stdout);
  }
}
