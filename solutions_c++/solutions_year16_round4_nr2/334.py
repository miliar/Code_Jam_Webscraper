#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long lint;

const int MAX_N = 205;

double dp[MAX_N][MAX_N];
double p[MAX_N], ps[MAX_N];

double dfs(int i, int j) {
  if (i < 0 || j < 0 || j > i) return 0;
  if (i == 0) return 1;
  double &ans = dp[i][j];
  if (ans != -1) return ans;
  return ans = dfs(i - 1, j - 1) * ps[i] + dfs(i - 1, j) * (1 - ps[i]);
}

double solve() {
  int n, k;
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%lf", &p[i]);
  }
  sort(p + 1, p + n + 1);
  double ans = 0;
  for (int i = k; i <= n; ++i) {
    copy(p + i - k + 1, p + i + 1, ps + 1);
    fill(dp[0], dp[n + 1], -1.0);
    check_max(ans, dfs(k, k / 2));
  }
  for (int i = 0; i <= k; ++i) {
    copy(p + 1, p + i + 1, ps + 1);
    copy(p + n + 1 - (k - i), p + n + 1, ps + i + 1);
    fill(dp[0], dp[n + 1], -1.0);
    check_max(ans, dfs(k, k / 2));
  }
  return ans;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %.20lf\n", index, solve());
  }
  return 0;
}
