#include <cstdio>

using namespace std;

#define MAXN 1010

char s[MAXN];

int main() {
  int nt, nteste=1, n, cnt, ans;
  scanf("%d", &nt);
  while (nt--) {
    scanf("%d", &n);
    scanf(" %s", s);
    cnt = ans = 0;
    for (int i=0; i<=n; i++) {
      int k = s[i]-'0';
      while (k--) {
        if (cnt < i) ans += i-cnt, cnt += i-cnt;
        cnt++;
      }
    }
    printf("Case #%d: %d\n", nteste++, ans);
  }

  return 0;
}