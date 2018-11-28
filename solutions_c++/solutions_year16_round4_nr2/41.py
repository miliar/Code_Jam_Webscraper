#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
typedef int64_t i64;

double DP[300][300];
double solve(const vector<double>& P, i64 at, i64 yes) {
  if (DP[at][yes] != -1)
    return DP[at][yes];
  if (at == P.size())
    return yes * 2 == P.size() ? 1 : 0;
  double ans = P[at] * solve(P, at + 1, yes + 1);
  ans += (1 - P[at]) * solve(P, at + 1, yes);
  DP[at][yes] = ans;
  return ans;
}

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    i64 N, K;
    scanf("%lld %lld ", &N, &K);
    vector<double> P(N);
    for (i64 i = 0; i < N; i++)
      scanf("%lf", &P[i]);
    sort(P.begin(), P.end());

    double ans = 0.0;
    for (i64 i = 0; i <= K; i++) {
      vector<double> test;
      for (i64 j = 0; j < i; j++)
        test.push_back(P[j]);
      for (i64 j = N - 1; test.size() < K; j--)
        test.push_back(P[j]);
      for (i64 j = 0; j < 300; j++)
        for (i64 k = 0; k < 300; k++)
          DP[j][k] = -1;
      ans = max(ans, solve(test, 0, 0));
    }

    printf("Case #%lld: %.09lf\n", zz, ans);
  }
}
