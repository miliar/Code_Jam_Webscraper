#include <cstdio>

int T;

bool is_palin(int v) {
  char dd[100];
  int l = 0;

  if (v == 0) return true;

  while (v) {
    dd[l++] = v % 10;
    v /= 10;
  }

  int i = 0, j = l - 1;
  while (i < j) {
    if (dd[i] != dd[j]) return false;
    i++;
    j--;
  }

  return true;
}

int main() {

  scanf("%d", &T);

  for (int tt = 1; tt <= T; tt++) {
    int A, B;
    scanf("%d %d", &A, &B);

    int num = 0;

    for (int s = 0; s * s <= B; s++) {
      int ss = s * s;
      if (ss < A) continue;
      if (is_palin(s) && is_palin(ss)) num++;
    }

    printf("Case #%d: %d\n", tt, num);
  }
  

  return 0;
}
