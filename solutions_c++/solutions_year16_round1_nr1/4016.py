#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[1001];

void solve(char *l, char *r) {
  if (l == r)
    return;
  char m = 0;
  for (char *p = l; p < r; p++)
    m = max(m, *p);
  for (char *p = l; p < r; p++)
    if (*p == m)
      putchar(m);
  
  char *p = l;
  while (*p != m)
    p++;
  solve(l, p);
  while (p < r) {
    if (*p != m)
      putchar(*p);
    p++;
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    scanf("%s", s);
    printf("Case #%d: ", i);
    solve(s, s + strlen(s));
    putchar('\n');
  }
}
