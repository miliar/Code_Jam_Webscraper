#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int kMax = 60;

struct Cntr {
  int v[kMax];
};
int N;
int H[kMax][kMax];
Cntr L[kMax * 2];
int A[2][kMax]; // 0: row; 1: col

bool cmp(Cntr &ac, Cntr &bc) {
  auto a = ac.v, b = bc.v;
  for (int i = 0; i < N; ++i) {
    if (a[i] == b[i]) continue;
    return a[i] < b[i];
  }
  return 0;
}

bool match_col(int n, int r) {
  for (int i = 0; i < N; ++i) {
    if (A[0][i] < 0) continue;
    auto v = L[A[0][i]].v;
    if (v[n] != L[r].v[i]) return false;
  }
  return true;
}

bool match_row(int n, int r) {
  for (int i = 0; i < N; ++i) {
    if (A[1][i] < 0) continue;
    auto v = L[A[1][i]].v;
    if (v[n] != L[r].v[i]) return false;
  }
  return true;
}

bool solve(int i) {
  if (i >= 2 * N - 1) return true;
  for (int j = 0; j < N; ++j) {
    if (A[0][j] < 0) {
      if (match_row(j, i)) {
        A[0][j] = i;
        if (solve(i + 1)) return true;
        A[0][j] = -1;
      }
    }
    if (A[1][j] < 0) {
      if (match_col(j, i)) {
        A[1][j] = i;
        if (solve(i + 1)) return true;
        A[1][j] = -1;
      }
    }
  }
  return false;
}

int main() {
  int t;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++i) {
    scanf("%d", &N);
    memset(A, -1, sizeof(A));
    for (int g = 0; g < 2 * N - 1; ++g) {
      for (int n = 0; n < N; ++n) scanf("%d", &L[g].v[n]);
    }

    printf("Case #%d:", i);

    sort(&L[0], &L[2 * N - 1], cmp);
    solve(0);

    for (int i = 0; i < N; ++i) {
      if (A[0][i] < 0) {
        for (int j = 0; j < N; ++j) {
          printf(" %d", L[A[1][j]].v[i]);
        }
        goto next;
      }
    }

    for (int i = 0; i < N; ++i) {
      if (A[1][i] < 0) {
        for (int j = 0; j < N; ++j) {
          printf(" %d", L[A[0][j]].v[i]);
        }
        goto next;
      }
    }

next:
    printf("\n");
  }

  return 0;
}
