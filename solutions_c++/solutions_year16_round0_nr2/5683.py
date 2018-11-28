#include <cstdio>
#include <cstring>

int T, tt;
char s[200];

void solve() {
  scanf("%s", s);
  int res = 0;
  int next;
  for(next = 1; s[next] != '\0' && s[next] == s[next-1]; next++)
    ;
  while(s[next] != '\0') {
    res++;
    for(next = next + 1; s[next] != '\0' && s[next] == s[next-1]; next++)
      ;
  }
  if(s[next-1] == '-')
    res++;
  printf("%d\n", res);
}

int main() {
  scanf("%d", &T);
  for(tt = 1; tt <= T; tt++) {
    printf("Case #%d: ", tt);
    solve();
  }
  return 0;
}
