#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

typedef long long LL;
const int maxn = 15;
bool vis[maxn];

int check(LL k) {
  int res = 0;
  while (k) {
    int x = k % 10;
    k /= 10;
    if (!vis[x]) {
      ++res;
      vis[x] = true;
    }
  }
  return res;
}

int main() {
  freopen("A-large.in.txt", "r", stdin);
  freopen("A-large.out.txt", "w", stdout);
  int t, tt = 0;
  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", ++tt);
    if (n == 0) {
      puts("INSOMNIA");
      continue;
    }
    LL ans = n;
    memset(vis, 0, sizeof vis);
    int cnt = 0;
    for (;;) {
      cnt += check(ans);
      if (cnt == 10) {
        break;
      }
      ans += n;
    }
    printf("%lld\n", ans);
  }
  return 0;
}

