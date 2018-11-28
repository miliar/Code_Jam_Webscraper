#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())

typedef long long ll;

typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

void solve() {
  ll b;
  int n;
  scanf("%I64d%d", &b, &n);
  vll as(n);
  for (int i = 0; i < n; i++)
    scanf("%I64d", &as[i]);
  while (sz(as) < 37)
    as.pb(0);
  sort(as.begin(), as.end());

  n = sz(as);

  double ans = 0;
  for (int cnt = 1; cnt <= n; cnt++) {
    for (int lasup = cnt; lasup <= n; lasup++) {
      ll minlev = as[cnt - 1];
      if (cnt < lasup) minlev = max(minlev, as[lasup - 1]);

      ll curbud = 0;
      for (int i = 0; i < cnt; i++)
        curbud += minlev - as[i];
      ll curbet = curbud;

      for (int i = cnt; i < lasup; i++)
        if (as[i] <= minlev) {
          curbud += minlev + 1 - as[i];
        }
      ll maxlev = ll(1e18);
      if (lasup < n) maxlev = as[lasup] - 1;

      if (curbud > b) continue;
      maxlev = min(maxlev, minlev + (b - curbud) / lasup);

      if (minlev > maxlev) continue;

      for (int k = 0; k < 2; k++) {
        ll curlev = k == 0 ? minlev : maxlev;
        ll cbud = curbud + (curlev - minlev) * lasup;
        ll cbet = curbet + (curlev - minlev) * cnt;
        assert(cbud <= b);
        double cans = 36.0 * cbet / cnt - cbud;
        ans = max(ans, cans);
      }
//      cans = 36 * (cbet + x * cnt) / cnt - (cbud + lasup * x)
    }
  }
  printf("%.18lf\n", ans);
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "";
    if (argc >= 2) fn = argv[1];
    if (endsWith(fn, ".in")) fn = string(fn, 0, fn.length() - 3);
    freopen((fn + ".in").c_str(), "r", stdin);
    freopen((fn + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    eprintf("Case #%d:\n", TN);
    printf("Case #%d: ", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Catched exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
