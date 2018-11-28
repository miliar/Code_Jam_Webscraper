#include <bits/stdc++.h>

using namespace std;

#define next NEXT

const int inf = 1 << 29;
const int mod = 1000000007;

char s[9][20];
int tree[1000][26], next;
int pre[1 << 8];
int dp[9][1 << 8];
long long dp2[9][1 << 8][1000];

int solve(int rem, int msk) {
  if(!rem) return msk ? -inf : 0;
  int &res = dp[rem][msk];
  if(res != -1) return res;
  res = -inf;
  for(int sub = msk; sub > 0; sub = (sub - 1) & msk) {
    int next = (~sub) & msk;
    res = max(res, solve(rem - 1, next) + pre[sub]);
  }
  return res;
}

long long solve2(int rem, int msk, int remNodes) {
  if(!rem) return !msk && !remNodes;
  long long &res = dp2[rem][msk][remNodes];
  if(res != -1) return res;
  res = 0;
  for(int sub = msk; sub > 0; sub = (sub - 1) & msk) {
    int next = (~sub) & msk;
    if(pre[sub] <= remNodes) {
      res += solve2(rem - 1, next, remNodes - pre[sub]);
      res %= mod;
    }
  }
  return res;
}

int main() {
  freopen("D-small-attempt1.in", "rt", stdin);
  freopen("D-small-attempt1.out", "wt", stdout);
  int t; scanf("%d", &t);
  for(int tst = 1; tst <= t; ++tst) {
    int m, n; scanf("%d %d", &m, &n);
    for(int i = 0; i < m; ++i)
      scanf("%s", s[i]);
    for(int msk = 1; msk < (1 << m); ++msk) {
      memset(tree, -1, sizeof tree);
      next = 1;
      for(int i = 0; i < m; ++i) if((msk >> i) & 1) {
        int root = 0;
        for(int j = 0; s[i][j]; ++j) {
          if(tree[root][s[i][j] - 'A'] == -1)
            tree[root][s[i][j] - 'A'] = next++;
          root = tree[root][s[i][j] - 'A'];
        }
      }
      pre[msk] = next;
    }
    memset(dp, -1, sizeof dp);
    int maxNodes = solve(n, (1 << m) - 1);
    memset(dp2, -1, sizeof dp2);
    long long count = solve2(n, (1 << m) - 1, maxNodes);
    printf("Case #%d: %d %lld\n", tst, maxNodes, count);
  }
  return 0;
}
