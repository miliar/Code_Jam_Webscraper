#include <cstdio>

int T, tt;
int n;
int m[20000];

void solve(int tt) {

  scanf("%d", &n);
  int i;
  for(i = 0; i < n; i++)
    scanf("%d", &m[i]);

  int a = 0;
  for(i = 0; i+1 < n; i++)
    if(m[i+1] < m[i])
      a += m[i] - m[i+1];

  int b = 0;
  int rate = -1;
  int j = 0;
  for(i = 0; i+1 < n; i++)
    if(m[i]-m[i+1] > rate) {
      rate = m[i]-m[i+1];
      j = i+1;
    }

  int remain = 0;
  for(i = 0; i+1 < n; i++) {
    if(remain < m[i])
      remain += m[i]-remain;
    if(remain < rate) {
      b += remain;
      remain = 0;
    }
    else {
      b += rate;
      remain -= rate;
    }
  }
  printf("Case #%d: %d %d\n", tt, a, b);
}

int main() {

  scanf("%d", &T);
  for(tt = 1; tt <= T; tt++)
    solve(tt);
  return 0;
}
