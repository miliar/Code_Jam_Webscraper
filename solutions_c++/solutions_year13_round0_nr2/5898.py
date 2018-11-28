#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 101

int cmp(const void *a, const void *b) {
  int *aa = (int *)a;
  int *bb = (int *)b;
  return *bb - *aa;
}

bool check() {
  int n, m, i, j;
  int idx = 0;
  int arr[MAX*MAX][3];
  int flag[MAX][2];
  scanf("%d %d", &n, &m);
  for (i = 0;i < n; ++i) {
    for (j = 0;j < m; ++j) {
      scanf("%d", &arr[idx][0]);
      arr[idx][1] = i;
      arr[idx][2] = j;
      ++idx;
    }
  }
  qsort(arr, n*m, sizeof(arr[0]), cmp);
  memset(flag, -1, sizeof(flag));
  for (i = 0;i < n*m; ++i) {
    //printf("%d %d %d\n", arr[i][0], arr[i][1], arr[i][2]);
    int count = 0;
    for (j = 0;j < 2; ++j) {
      int p = arr[i][j+1];
      if (flag[p][j] != -1 && arr[i][0] < flag[p][j]) {
        count += 1;
      } else {
        flag[p][j] = arr[i][0];
      }
    }
    if (count == 2) return false;
  }
  return true;
}

int main() {
  int t ;
  scanf("%d", &t);
  for (int i = 1;i <= t; ++i) {
    printf("Case #%d: ", i);
    if (check()) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
  return 0;
}

