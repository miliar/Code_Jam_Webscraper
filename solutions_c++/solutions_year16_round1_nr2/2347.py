#include <bits/stdc++.h>
using namespace std;

int T, N, H[105][55], m[55], k[55], ans[55], f1, f2, v[105];

void dfs2(int cnt) {
  if (f2) return;
  if (cnt == N-1) {
    int r = 0;
    while (k[r]) {
      r++;
    }
    for (int i = 0; i < N; i++) {
      ans[i] = H[m[i]][r];
    }
    f2 = 1;
    return;
  }
  for (int i = 0; i < 2*N-1; i++) {
    if (v[i]) continue;
    for (int j = 0; j < N; j++) {
      if (k[j]) continue;
      int flag = 1;
      for (int l = 0; l < N; l++) {
        if (H[m[l]][j] == H[i][l]) continue;
        flag = 0;
        break;
      }
      if (flag) {
        v[i] = 1;
        k[j] = 1;
        dfs2(cnt+1);
        k[j] = 0;
        v[i] = 0;
      }
    }
  }
}

void dfs1(int a[55], int row, int col) {
  if (f1) return;
  if (row == N) {
    dfs2(1);
    f1 = f2;
    return;
  }
  for (int i = 0; i < 2*N-1; i++) {
    if (!v[i] && H[i][col] == a[row]) {
      v[i] = 1;
      m[row] = i;
      dfs1(a, row+1, col);
      v[i] = 0;
    }
  }
}

int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d", &N);
    for (int i = 0; i < 2*N-1; i++) {
      for (int j = 0; j < N; j++) {
        scanf("%d", &H[i][j]);
      }
    }
    f1 = f2 = 0;
    for (int i = 0; i < 2*N-1 && !f1; i++) {
      for (int j = 0; j < 2*N-1; j++) {
        v[j] = 0;
      }
      for (int j = 0; j < N; j++) {
        m[j] = k[j] = 0;
      }
      v[i] = 1;
      for (int j = 0; j < N && !f1; j++) {
        k[j] = 1;
        dfs1(H[i], 0, j);
        k[j] = 0;
      }
      v[i] = 0;
    }
    printf("Case #%d:", t);
    for (int i = 0; i < N; i++) {
      printf(" %d", ans[i]);
    }
    printf("\n");
  }
  return 0;
}

