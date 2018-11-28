#include <cstdio>
#include <algorithm>

const int N = 30;

int n, m;

int adj[N];

bool flag[N];

int order[N];

bool dfs(int i) {
  if (i == n) return true;
  int a = order[i];
  bool t = false;
  for (int b = 0; b < n; ++b) {
    if (adj[a] >> b & 1) {
      if (!flag[b]) {
        flag[b] = true;
        if (!dfs(i + 1)) return false;
        t = true;
        flag[b] = false;
      }
    }
  }
  return t;
}

bool check(int s) {
  for (int i = 0; i < n; ++i) adj[i] = 0;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      if (s >> (i * n + j) & 1) adj[i] |= 1 << j;
  for (int i = 0; i < n; ++i) order[i] = i;
  do {
    for (int i = 0; i < n; ++i) flag[i] = false;
    if (!dfs(0)) return false;
  } while (std::next_permutation(order, order + n));
  return true;
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d", &n);
    int t = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        char x;
        scanf(" %c", &x);
        if (x == '1') t |= 1 << (i * n + j);
      }
    }
    m = n * n;
    int ans = m;
    for (int s = 0; s < (1 << m); ++s) {
      if ((s & t) != t) continue;
      int cur = __builtin_popcount(s ^ t);
      if (cur >= ans) continue;
      if (check(s)) ans = cur;
    }
    printf("Case #%d: %d\n", tid, ans);
  }
  return 0;
}
