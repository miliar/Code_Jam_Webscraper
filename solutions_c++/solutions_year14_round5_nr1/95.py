#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    long long N, p, q, r, s;
    scanf("%lld", &N);
    scanf("%lld%lld%lld%lld", &p, &q, &r, &s);

    vector<long long> F;
    vector<long long> P(1, 0);
    for (int i = 0; i < N; i++) {
      long long v = (i * p + q) % r + s;
      F.push_back(v);
      P.push_back(P.back() + v);
    }

    long long best = P[N];

    for (int a = 0; a < N; a++) {
      int lo = a + 1, hi = N;
      while (lo != hi) {
        int mid = (lo + hi) / 2;
        if (P[mid] - P[a] >= P[N] - P[mid])
          hi = mid;
        else
          lo = mid + 1;
      }
      for (int u = lo - 4; u <= lo + 4; u++) {
        if (u < a+1 || u > N) continue;
        long long cur = max(P[a], max(P[u] - P[a], P[N] - P[u]));
        if (cur < best) best = cur;
      }
    }

    printf("Case #%d: %.12lf\n", tc, (P[N] - best) * 1.0 / P[N]);
  }
}
