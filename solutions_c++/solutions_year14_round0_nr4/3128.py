#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX 1024

void input(void);
void solve(void);

int n;
double A[MAX];
double B[MAX];
int used[MAX];
int case_cnt = 1;

int main(void) {
  int t;
  scanf("%d", &t);
  while (t--) {
    input();
    solve();
  }
  return 0;
}

void input(void) {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%lf", &A[i]);
  for (int i = 0; i < n; i++) scanf("%lf", &B[i]);
}

void solve(void) {
  sort(A, A + n);
  sort(B, B + n);
  int p1 = 0;
  int j = 0;
  for (int i = 0; i < n; i++) {
    if (A[i] > B[j]) {
      j++;
      p1++;
    }
  }
  int p2 = 0;
  memset(used, 0, sizeof(used));
  for (int i = n - 1; i >= 0; i--) {
    for (j = 0; j < n; j++) {
      if (used[j]) continue;
      if (A[i] < B[j]) break;
    }
    if (j < n) {
      used[j] = 1;
    } else {
      p2++;
      for (j = 0; j < n; j++) {
        if (used[j]) continue;
        used[j] = 1;
        break;
      }
    }
  }
  printf("Case #%d: %d %d\n", case_cnt++, p1, p2);
}

