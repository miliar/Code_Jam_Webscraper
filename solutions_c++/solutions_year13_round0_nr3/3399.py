#include <cstdio>
#include <cstring>

typedef long long LL;

LL a[12] = {1, 4, 9, 121, 484, 12321, 1234321, 123454321, 12345654321ll, 1234567654321ll, 123456787654321ll, 12345678987654321ll};
LL A, B;
char s[100000], t[100000];

int main() {
  int cas = 0;
  int T; scanf("%d", &T);
  while (T--) {
    scanf("%s", s);
    scanf("%s", t);
    if (strlen(s) > 17) A = 12345678987654321ll;
    else sscanf(s, "%lld", &A);
    if (strlen(t) > 17) B = 12345678987654321ll;
    else sscanf(t, "%lld", &B);
    int cnt = 0;
    for (int i = 0; i < 12; ++i) {
      if (A <= a[i] && a[i] <= B) ++cnt;
    }
    printf("Case #%d: %d\n", ++cas, cnt);
  }
  return 0;
}
