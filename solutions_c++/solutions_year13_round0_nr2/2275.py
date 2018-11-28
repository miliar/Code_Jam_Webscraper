#include <stdio.h>

const int MAX_N = 110;
const int MAX_M = 110;

int n, m;
int grass[MAX_N][MAX_M];

bool solve() {

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      bool larger_l = false, larger_c = false;
      for (int k = 0; k < n; k++)
        if (grass[k][j] > grass[i][j])
          larger_l = true;
      for (int k = 0; k < m; k++)
        if (grass[i][k] > grass[i][j])
          larger_c = true;
      if (larger_c && larger_l)
        return false;
    }
  }

  return true;
}

int main(int argc, char *argv[])
{

  int nt;
  scanf("%d", &nt);

  for (int t = 1; t <= nt; t++) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        scanf("%d", &grass[i][j]);
      }
    }

    printf("Case #%d: %s\n", t, solve() ? "YES" : "NO" );
  }

  return 0;
}
