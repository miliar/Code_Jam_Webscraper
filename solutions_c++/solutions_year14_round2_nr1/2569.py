#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 101

int getDiff(char a[MAX], char b[MAX]) {
  int i, j, diff = 0;
  for (i = 0, j = 0;; ++i, ++j) {
    while (b[j] != a[i]) {
      if (b[j-1] == b[j])
      {
        ++j;
        ++diff;
      }
      else {
        ++diff;
        --j;
        break;
      }
    }
    if (a[i] == '\0') break;
  }
  return diff;
}

int getRes(char str[MAX][MAX], int n) {
  int i, j, idx;
  char tmp[MAX];
  char s[MAX];
  int len[MAX];
  for (i = 0;i < n; ++i) {
    tmp[0] = str[i][0];
    idx = 1;
    for (j = 1; str[i][j] != '\0'; ++j) {
      if (str[i][j] != str[i][j-1]) {
        tmp[idx++] = str[i][j];
      }
    }
    tmp[idx] = '\0';
    if (i == 0) {
      strcpy(s, tmp);
    } else {
      if (strcmp(tmp, s) != 0) {
        return -1;
      }
    }
    len[i] = strlen(str[i]);
  }
  int d[MAX][MAX];
  memset(d, -1, sizeof(d));
  int diff = 0;
  int res = 1000000000;
  for (i = 0;i < n; ++i) {
    diff = 0;
    for (j = 0;j < n; ++j) {
      if (d[i][j] == -1) d[i][j] = d[j][i] = getDiff(str[i], str[j]);
      diff += d[i][j];
    }
    if (diff < res) res = diff;
  }
  return res;
}

int main() {
  int T, n, m;
  scanf("%d", &T);
  int i, j, k, res;
  char str[MAX][MAX];
  for (i = 1;i <= T; ++i) {
    res = -1;
    scanf("%d", &n);
    for (j = 0;j < n; ++j) {
      scanf("%s", str[j]);
    }
    res = getRes(str, n);
    printf("Case #%d: ", i); 
    if (res == -1) 
      printf("Fegla Won\n"); 
    else 
      printf("%d\n", res);
  }
  return 0;
}

