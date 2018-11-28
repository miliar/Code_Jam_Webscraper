#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

namespace {

double Solve(vector<double> P, int K) {
  const int N = P.size();
  sort(P.begin(), P.end());
  double res = 0.0;
  for (int i = 0; i <= K; ++i) {
    vector<double> mem(K + 1);
    mem[0] = 1.0;
    for (int j = 0; j < N; ++j) {
      if (j >= i && j < N - (K - i)) continue;
      vector<double> mem1(K + 1);
      for (int k = 0; k < K; ++k) {
        mem1[k] += mem[k] * (1.0 - P[j]);
        mem1[k + 1] += mem[k] * P[j];
      }
      mem = mem1;
    }
    res = max(res, mem[K / 2]);
  }
  return res;
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, K;
    cin >> N >> K;
    vector<double> P(N);
    for (int j = 0; j < N; ++j) cin >> P[j];
    cout << "Case #" << i << ": " << Solve(P, K) << endl;
  }

  return 0;
}
