#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  for (int Case = 1; Case <= n_cases; ++Case) {
    printf("Case #%d: ", Case);
    int n;
    scanf("%d", &n);
    vector<double> A(n), B(n);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &A[i]);
    }
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &B[i]);
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    int i = 0;
    while (i < n) {
      bool done = true;
      for (int i_ = i, j_ = 0; i_ < n; ++i_, ++j_) {
        if (A[i_] < B[j_]) {
          done = false;
          break;
        }
      }
      if (done) {
        break;
      } else {
        ++i;
      }
    }
    printf("%d ", n - i);
    vector<bool> used(n, false);
    int score = 0;
    for (int i = 0; i < n; ++i) {
      bool lost = false;
      for (int j = 0; j < n; ++j) {
        if (!used[j] && B[j] > A[i]) {
          used[j] = true;
          lost = true;
          break;
        }
      }
      if (!lost) {
        ++score;
        for (int j = 0; j < n; ++j) {
          if (!used[j]) {
            used[j] = true;
            break;
          }
        }
      }
    }
    printf("%d\n", score);
  }
  return 0;
}
