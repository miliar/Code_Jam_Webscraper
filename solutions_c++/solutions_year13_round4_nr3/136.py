#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 5050;

int a[MAXN], b[MAXN];

bool gt[MAXN][MAXN];

int main() {
  int re, n;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; ++i) {
      scanf("%d", &b[i]);
    }
    fill(gt[0], gt[n], false);

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        if (a[j] >= a[i]) {
          gt[j][i] = true;
        }
      }
      for (int j = i + 1; j < n; ++j) {
        if (b[j] >= b[i]) {
          gt[j][i] = true;
        }
      }
    }

    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          gt[i][j] = gt[i][j] || (gt[i][k] && gt[k][j]);
        }
      }
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        putchar(gt[i][j] ? '>' : ' ');
      }
      puts("");
    }
  }

  return 0;
}

