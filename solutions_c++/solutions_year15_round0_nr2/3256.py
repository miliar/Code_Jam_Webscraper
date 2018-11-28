#include <iostream>
using namespace std;
int P[1111];
int main() {
  int tt = 0;
  int T;
  cin >> T;
  for (int tt = 0; tt < T; tt++) {
    int D;
    cin >> D;
    int M = 0;
    for (int i = 0; i < D; i++) {
      cin >> P[i];
      M = max(M, P[i]);
    }
    int ans = 1111;
    for (int i = 1; i <= M; i++) {
      int t = i;
      for (int j = 0; j < D; j++) {
        if (P[j] > i) {
          t += (P[j] - 1) / i;
        }
      }
      ans = min(ans, t);

    }
    printf("Case #%d: %d\n", tt+1, ans);
  }
}
