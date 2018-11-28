#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define image(a) {sort(all(a)), a.resize(unique(all(a)) - a.begin());}
ld dp[210][210];
void solve() {
  int n, k;
  cin >> n >> k;
  vector<ld> p(n);
  for (int i = 0; i < n; i++) {
    cin >> p[i];
  }
  sort(all(p));
  ld ans = 0;
  for (int i = 0; i <= k; i++) {
    vector<ld> a;
    for (int j = 0; j < i; j++) {
      a.pb(p[j]);
    }
    for (int j = 0; j < k - i; j++) {
      a.pb(p[n - 1 - j]);
    }
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int j = 0; j < k; j++) {
      for (int s = 0; s <= j; s++) {
        dp[j + 1][s + 1] += dp[j][s] * a[j];
        dp[j + 1][s] += dp[j][s] * (1 - a[j]);
      }
    }
    if (dp[k][k / 2] > ans) {
      ans = dp[k][k / 2];
    }
  }
  printf("%.18lf\n", (double)ans);
}

int main(){
  assert(freopen("a2.out","wt",stdout));
  assert(freopen("a.in","rt",stdin));
  int T;
  scanf("%d", &T);
  for (int ti = 1; ti <= T; ti++) {
    printf("Case #%d: ", ti);
    solve();
  }
  return 0;
}
