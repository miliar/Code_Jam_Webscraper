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
vector<int> dp[100][3];
vector<int> conc(vector<int> a, vector<int> b) {
  for (int x : b) {
    a.pb(x);
  }
  return a;
}
vector<int> calc(int n, int x) {
  if (n == 0) {
    vector<int> res;
    res.pb(x);
    return res;
  }
  if (sz(dp[n][x]) == 0) {
    if (x == 0) {
      vector<int> s1 = calc(n - 1, 0);
      vector<int> s2 = calc(n - 1, 1);
      dp[n][x] = min(conc(s1, s2), conc(s2, s1));
    }
    if (x == 1) {
      vector<int> s1 = calc(n - 1, 1);
      vector<int> s2 = calc(n - 1, 2);
      dp[n][x] = min(conc(s1, s2), conc(s2, s1));
    }
    if (x == 2) {
      vector<int> s1 = calc(n - 1, 0);
      vector<int> s2 = calc(n - 1, 2);
      dp[n][x] = min(conc(s1, s2), conc(s2, s1));
    }
  }
  return dp[n][x];
}
void solve() {
  int n;
  cin >> n;
  string S = "PRS";
  vector<int> a(n + 1);
  vector<int> b(n + 1);
  vector<int> c(n + 1);
  cin >> b[0] >> a[0] >> c[0];
  for (int i = 0; i < n; i++) {
    int s = (a[i] + b[i] + c[i]) / 2;
    a[i + 1] = s - c[i];
    b[i + 1] = s - a[i];
    c[i + 1] = s - b[i];
    if (a[i + 1] < 0 || b[i + 1] < 0 || c[i + 1] < 0) {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  vector<int> cur;
  if (a[n] == 1) {
    cur = calc(n, 0);
  }
  if (b[n] == 1) {
    cur = calc(n, 1);
  }
  if (c[n] == 1) {
    cur = calc(n, 2);
  }
  for (int i = 0; i < sz(cur); i++) {
    printf("%c", S[cur[i]]);
  }
  printf("\n");
}                               

int main(){
  assert(freopen("a.out","wt",stdout));
  assert(freopen("a.in","rt",stdin));
  int T;
  scanf("%d", &T);
  for (int ti = 1; ti <= T; ti++) {
    printf("Case #%d: ", ti);
    solve();
  }
  return 0;
}
