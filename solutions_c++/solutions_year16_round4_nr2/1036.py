#include <iostream>
#include <algorithm>
using namespace std;

int T, N, K;
double P[300];

void each_case()
{
  double ans = 0.0;

  for (int i = 0; i < (1 << N); ++i) {
    int ii = i;
    int cnt = 0;
    while (ii) {
      cnt += ii % 2;
      ii /= 2;
    };
    if (cnt != K) continue;

    double Q[300][300];
    Q[0][0] = 1.0;
    for (int k = 1; k <= N; ++k) Q[0][k] = 0.0;
    for (int n = 1; n <= N; ++n) {
      if (i & (1 << (n - 1))) {
        for (int k = 0; k <= N; ++k) Q[n][k] = (1 - P[n]) * Q[n - 1][k];
        for (int k = 1; k <= N; ++k) Q[n][k] += P[n] * Q[n - 1][k - 1];
      } else {
        for (int k = 0; k <= N; ++k) Q[n][k] = Q[n - 1][k];
      }
    }
    ans = max(ans, Q[N][K / 2]);
  }

  cout.precision(16);
  cout << " " << ans;
}

int main()
{
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ":";

    cin >> N >> K;
    for (int j = 1; j <= N; ++j)
      cin >> P[j];
    each_case();

    cout << endl;
  }

  return 0;
}
