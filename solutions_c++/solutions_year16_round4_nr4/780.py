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
    int N; cin >> N;
    vector<int> A(N, 0);

    int msk = 0;
    int result = N * N;
    for (int i = 0; i < N; i++) {
      string S; cin >> S;
      for (int j = 0; j < N; j++) {
        if (S[j] == '1') {
          A[i] |= 1 << j;
          msk |= 1 << i * N + j;
        }
      }
    }

    for (int i = msk; i < 1 << N * N; i = (i + 1) | msk) {
      for (int j = 0; j < N; j++) {
        A[j] = (i >> j * N) & (1 << N) - 1;
      }

      bool allok = true;
      for (int j = 0; j < N; j++) {
        int ws = 0;
        for (int k = 0; k < N; k++) {
          if (A[k] & 1 << j) {
            ws |= 1 << k;
          }
        }

        bool ok = false;
        for (int sws = ws; sws; sws = sws - 1 & ws) {
          int cn = 0;
          for (int k = 0; k < N; k++) {
            if (sws & 1 << k) {
              cn |= A[k];
            }
          }
          if (__builtin_popcount(cn) <= __builtin_popcount(sws)) {
            ok = true;
          }
        }
        if (!ok) {
          allok = false;
        }
      }
      if (allok) {
        result = min(result, __builtin_popcount(i) - __builtin_popcount(msk));
      }
    }

    cout << "Case #" << t << ": " << result << endl;
  }
  return 0;
}
