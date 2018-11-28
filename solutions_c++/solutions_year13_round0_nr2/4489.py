#include<cstdio>

const int MAXN = 100;

int n, m;
int A[MAXN+1][MAXN+1];

bool check() {
  bool flag;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      flag = true;
      for (int k = 0; k < m; k++) {
        if (A[i][j] < A[i][k]) { flag = false; }
      }
      if (flag) { continue; }

      flag = true;
      for (int k = 0; k < n; k++) {
        if (A[i][j] < A[k][j]) { flag = false; }
      }

      if (! flag) { return false; }
    }
  }
  return true;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int Z = 1; Z <= T; Z++) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        scanf("%d", &A[i][j]);
      }
    }

    printf("Case #%d: ", Z);
    if (check()) { printf("YES"); }
    else { printf("NO"); }

    printf("\n");
  }
  return 0;
}
