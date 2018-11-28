#include <stdio.h>
// #define DEBUG

#define MAX 1000000
// #define MAX 100

int queue[MAX+1];
int p, q;
int table[MAX+1];

void put(int n, int next) {
#ifdef DEBUG
  printf("n:%d next:%d\n", n, next);
#endif
  if (1<=next && next <= MAX) {
    if (table[next] == -1) {
      table[next] = table[n] + 1;
      queue[p++] = next;
    }
  }
}

int reverse(int n) {
#ifdef DEBUG
  printf("before reverse: %d ", n);
#endif
  int r = 0;
  while(n) {
    r = r * 10 + n %10;
    n /= 10;
  }
#ifdef DEBUG
  printf("after reverse: %d\n", r);
#endif
  return r;
}

int main()
{
  int T;
  for (int i = 1; i <= MAX; ++i) {
    table[i] = -1;
  }
  table[1] = 1;
  queue[0] = 1;
  p = 1; q = 0;
  int n, next;
  while (p > q) {
    n = queue[q++];
#ifdef DEBUG
    printf("current: %d\n", n);
#endif
    put(n, n+1);
    put(n, reverse(n));
  }

  scanf("%d", &T);
for (int ic = 1; ic <= T; ++ic) {
  int N;
  scanf("%d", &N);
  printf("Case #%d: %d\n", ic, table[N]);
}
  return 0;
}
