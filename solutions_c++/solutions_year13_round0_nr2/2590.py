#include <cstdio>
#include <vector>

using namespace std;

int main() {
  vector<bool> *w;
  bool ans, maxr, maxc;
  int n, m, i, j, k, l, t, **a;

  scanf("%d", &t);
  for (i = 1; i <= t; ++i) {
    scanf("%d%d", &n, &m);
    a = new int*[n];
    w = new vector<bool>[n];
    for (j = 0; j < n; ++j) {
      a[j] = new int[m];
      w[j].resize(m);
      for (k = 0; k < m; ++k) {
        scanf("%d", a[j] + k);
      }
    }

    ans = true;
    for (j = 0; j < n; ++j) {
      for (k = 0; k < m; ++k) {
        maxc = true;
        for (l = 0; l < n; ++l) {
          if (a[j][k] < a[l][k]) {
            maxc = false;
            break;
          }
        }
        maxr = true;
        for (l = 0; l < m; ++l) {
          if (a[j][k] < a[j][l]) {
            maxr = false;
            break;
          }
        }
        if (!maxr && !maxc) {
          ans = false;
          j = n;
          k = m;
        }
      }
    }
    printf("Case #%d: %s\n", i, ans ? "YES" : "NO");

    /*// Top
    for (j = 0; j < m; ++j) {
      for (k = 0; k < n; ++k) {
        if (a[k][j] < a[0][j]) {
          break;
        }
        w[k][j] = true;
      }
    }

    // Right
    for (j = 0; j < n; ++j) {
      for (k = m - 1; k >= 0; --k) {
        if (a[j][k] < a[j][m - 1]) {
          break;
        }
        w[j][k] = true;
      }
    }

    // Bottom
    for (j = 0; j < m; ++j) {
      for (k = n - 1; k >= 0; --k) {
        if (a[k][j] < a[n - 1][j]) {
          break;
        }
        w[k][j] = true;
      }
    }

    // Left
    for (j = 0; j < n; ++j) {
      for (k = 0; k < m; ++k) {
        if (a[j][k] < a[j][0]) {
          break;
        }
        w[j][k] = true;
      }
    }

    ans = true;
    for (j = 0; j < n; ++j) {
      for (k = 0; k < m; ++k) {
        if (!w[j][k]) {
          ans = false;
          j = n;
          break;
        }
      }
    }*/


    for (j = 0; j < n; ++j) {
      delete[] a[j];
      w[j].clear();
    }
    delete[] a;
    delete[] w;
  }

  return 0;
}
