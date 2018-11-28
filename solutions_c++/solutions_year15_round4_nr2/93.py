#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;

class range {private: struct I{int x;int operator*(){return x;}bool operator!=(I& lhs){return x<lhs.x;}void operator++(){++x;}};I i,n;
public:range(int n):i({0}),n({n}){}range(int i,int n):i({i}),n({n}){}I& begin(){return i;}I& end(){return n;}};

void solve();

int main() {
  int T; cin >> T;
  for (int test : range(1, T+1)) {
    cout << "Case #" << test << ": ";
    solve();
  }
}

////////////////////////////////////////////////////////////////////////////////

struct Water {
  double V, K;
  bool operator<(const Water& rhs) const {
    return K < rhs.K;
  }
};

void solve() {
  int N; cin >> N;
  double V, K; cin >> V >> K;
  Water w[N];
  for (int i : range(N)) cin >> w[i].V >> w[i].K;

  // check impossible
  sort(w, w + N);
  if (K < w[0].K || w[N - 1].K < K) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  {
    double g = 0;
    for (int i : range(N)) g += w[i].V * (w[i].K - K);
    if (g < 0) {
      K = -K;
      for (int i : range(N)) w[i].K = -w[i].K;
    }
  }

  sort(w, w + N);

  double lo = 0, hi = N;
  double vsum = 0;
  for (int iter : range(1000)) {
    double mid = (lo + hi) / 2;
    int k = (int)floor(mid);
    double vk = w[k].V * (mid - (double)k);

    double g = 0;
    vsum = 0;
    for (int i : range(N)) {
      double v = 0;
      if (i < k) v = w[i].V;
      if (i == k) v = vk;
      g += v * (w[i].K - K);

      vsum += v;
    }

    if (g <= 1e-90) lo = mid;
    else hi = mid;
  }

  double res = V / vsum;
  printf("%.14lf\n", res);
}
