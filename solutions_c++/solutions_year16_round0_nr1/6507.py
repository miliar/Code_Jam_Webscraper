#include <bits/stdc++.h>

using namespace std;

bool vis[10];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T, cas = 0;
  scanf("%d", &T);
  while (T --) {
    long long n, sum = 0;
    scanf("%lld", &n);
    memset(vis, 0, sizeof vis);
    int cnt = 10;
    while (n && cnt) {
      sum += n;
      long long a = sum;
      while (a) {
        if (!vis[a % 10]) vis[a % 10] = 1, cnt --;
        a /= 10;
      }
    }
    printf("Case #%d: ", ++ cas);
    if (!n) puts("INSOMNIA");
    else printf("%lld\n", sum);
  }
  return 0;
}