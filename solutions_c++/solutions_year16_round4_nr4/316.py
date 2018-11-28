#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long lint;

int n, e[4][4];
vector<int> perm;
bool vis[4];

bool dfs(int i) {
  if (i == n) return true;
  int u = perm[i];
  bool got = false;
  REP (j, n) {
    if (vis[j] || !e[u][j]) continue;
    got = true;
    vis[j] = true;
    if (!dfs(i + 1)) return false;
    vis[j] = false;
  }
  return got;
}

int solve() {
  scanf("%d", &n);
  fill(e[0], e[n], 0);
  int already = 0;
  REP (i, n) {
    char s[10];
    scanf("%s", s);
    REP (j, n) {
      e[i][j] = s[j] - '0';
      already |= e[i][j] << (i * n + j);
    }
  }
  perm.resize(n);
  int ans = n * n;
  REP (mask, 1 << (n * n)) {
    if (mask & already) continue;
    int cb = __builtin_popcount(mask);
    if (cb >= ans) continue;
    REP (i, n * n) e[i / n][i % n] += (mask >> i) & 1;
    bool ok = true;
    REP (i, n) perm[i] = i;
    do {
      fill(vis, vis + n, false);
      if (!dfs(0)) {
        ok = false;
        break;
      }
    } while (next_permutation(ALL(perm)));
    if (ok) check_min(ans, cb);
    REP (i, n * n) e[i / n][i % n] -= (mask >> i) & 1;
  }
  return ans;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %d\n", index, solve());
  }
  return 0;
}
