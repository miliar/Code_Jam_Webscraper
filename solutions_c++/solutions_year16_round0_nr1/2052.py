#include <cstdio>
#include <cstring>
#include <set>

typedef long long LL;

int main() {
  int cas;
  scanf("%d", &cas);
  for (int t = 1; t <= cas; ++t) {
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", t);
    if (n == 0) puts("INSOMNIA");
    else {
      std::set<int> current;
      LL m = n;
      while (true) {
        for (LL x = m; x > 0; x /= 10) current.insert(x % 10);
        if (current.size() == 10) break;
        m += n;
      }
      printf("%lld\n", m);
    }
  }
  return 0;
}
