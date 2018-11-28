#include <bits/stdc++.h>

using namespace std;

const int N = 10;
bool vis[N];

bool done() {
  bool check = true;
  for (int i = 0; i < N; ++i)
    check &= vis[i];
  return check;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", tst++);
      continue;
    }
    memset(vis, 0, sizeof vis);
    int i = 0;
    while (!done()) {
      long long x = 1ll * n * i;
      while (x) {
        vis[x % 10] = 1;
        x /= 10;
      }
      ++i;
    }
    printf("Case #%d: %lld\n", tst++, 1ll * (i - 1) * n);
  }
}
