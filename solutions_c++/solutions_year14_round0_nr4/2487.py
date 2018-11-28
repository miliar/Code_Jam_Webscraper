#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>

#define N 1000

double a[N], b[N];
int A[N], B[N];
int currentcase;

int war (double* x, double* y, int n) {
  int j = 0, count = 0;
  for (int i = 0; j < n; i++) {
    for (; x[i] > y[j] && j < n; j++);
    if (j < n && x[i] < y[j]) {
      j++;
      count++;
    }
  }
  return n-count;
}
bool all_greater(double* x, double* y, int n) {
  for (int i = 0; i < n; i++) {
    if (x[i] < y[i]) {
      return false;
    }
  }
  return true;
}
int dwar (double* x, double* y, int n) {
  for (int i = 0; i < n; i++) {
    if (all_greater(x+i, y, n-i)) {
      return n - i;
    }
  }
  return 0;
}

int main (void) {
  int T;
  scanf("%d", &T);
  //printf("%d\n", T);
  for (currentcase = 1; currentcase <= T; ++currentcase) {
    int n;
    scanf("%d", &n);
    //printf("%d\n", n);
    for (int i = 0; i < n; i++) {
      scanf("%lf", &a[i]);
    }
    for (int i = 0; i < n; i++) {
      scanf("%lf", &b[i]);
    }
    std::sort(a, a+n);
    std::sort(b, b+n);
    /*int i = 0, j = 0;
    for (int k = 0; i < n || j < n; k++) {
      if (i == n || (j < n && b[j] < a[i])) {
        B[j++] = k;
      } else {
        A[i++] = k;
      }
    }
    for (int i = 0; i < n; i++) {
      fprintf(stdout, "%d%c", A[i], (i+1 == n) ? '\n' : ' ');
    }
    for (int i = 0; i < n; i++) {
      fprintf(stdout, "%d%c", B[i], (i+1 == n) ? '\n' : ' ');
    }*/
    printf("Case #%d: %d %d\n", currentcase, dwar(a, b, n), war(a, b, n));
  }
  return 0;
}
