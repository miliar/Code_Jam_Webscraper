#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1000;
int n;
double A[N], B[N];
bool viz[N];

int solve_normal() {
  memset(viz, 0, sizeof(viz));
  int ret = 0;
  for (int i = 0; i < n; i++) {
    int k = -1;
    for (int j = 0; j < n; j++) {
      if (!viz[j] && B[j] > A[i]) {
        k = j;
        break;
      }
    }
    if (k == -1) {
      for (int j = 0; j < n; j++) {
        if (!viz[j]) {
          k = j;
          ret++;
          break;
        }
      }
    }
    viz[k] = 1;
  }
  return ret;
}

int solve_deceit() {
  memset(viz, 0, sizeof(viz));
  int ret = 0;
  for (int i = 0; i < n; i++) {
    int k = -1;
    for (int j = 0; j < n; j++) {
      if (!viz[j] && B[j] < A[i]) {
        k = j;
        ret++;
        break;
      }
    }
    if (k == -1) {
      for (int j = n - 1; j >= 0; j--) {
        if (!viz[j] && B[j] > A[i]) {
          k = j;
          break;
        }
      }
    }
    viz[k] = 1;
  }
  return ret;
}

int main() {
  int T; cin >> T;
  for (int test = 0; test < T; test++) {
    memset(viz, 0, sizeof(viz));

    cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
      cin >> B[i];
    }

    sort(A, A + n);
    sort(B, B + n);

    printf("Case #%d: %d %d\n", test + 1, solve_deceit(), solve_normal());
  }
}
