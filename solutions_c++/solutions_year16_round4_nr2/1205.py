#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, K;
    cin >> N >> K;
    vector<double> A(N);
    for (int i = 0; i < N; i++) {
      cin >> A[i];
    }

    double result = 0;
    for (int i = 0; i < 1 << N; i++) {
      if (__builtin_popcount(i) != K) {
        continue;
      }

      vector<double> DP(K / 2 + 1);
      DP[0] = 1;

      for (int k = 0; k < N; k++) {
        if (i & 1 << k) {
          for (int j = K / 2; j >= 0; j--) {
            DP[j] *= (1 - A[k]);
            if (j > 0) {
              DP[j] += A[k] * DP[j - 1];
            }
          }
        }
      }

      result = max(result, DP[K / 2]);
    }
    cout << "Case #" << t << ": ";
    printf("%.9f\n", result);
  }
  return 0;
}
