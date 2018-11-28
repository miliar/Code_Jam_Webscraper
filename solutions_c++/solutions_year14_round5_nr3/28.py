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
#define forn(i, n) for (int i = 0; i < (n); i++)

typedef long long ll;

typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

vector<pii> evs;
vi cst;
int minfre;
int ans;

void go(int v, int cbal, int minbal) {
  minbal = min(minbal, cbal);
  if (v >= sz(evs)) {
    int tmp = cbal - minbal;
    int tmp2 = count(cst.begin(), cst.end(), 1);
//    assert(tmp == tmp2);
    ans = min(ans, tmp2);
    return;
  }

  for (int me = 0; me < sz(cst) && me <= minfre; me++) if (evs[v].second < 0 || evs[v].second == me) {
    if (cst[me] == evs[v].first) continue;

    int old = cst[me];
    cst[me] = evs[v].first;

    int old2 = minfre;
    minfre = max(minfre, me + 1);

    go(v + 1, cbal + evs[v].first, minbal);

    minfre = old2;
    cst[me] = old;
  }
}

void solve() {
  int n;
  scanf("%d", &n);
  evs = vector<pii>(n);
  vi ids;
  for (pii &e : evs) {
    char op; int id;
    assert(scanf(" %c%d", &op, &id) == 2);
    id--;
    e = mp(op == 'E' ? +1 : -1, id);
    if (id >= 0) ids.pb(id);
  }

  sort(ids.begin(), ids.end());
  ids.erase(unique(ids.begin(), ids.end()), ids.end());
  for (pii &e : evs)
    if (e.second >= 0)
      e.second = lower_bound(ids.begin(), ids.end(), e.second) - ids.begin();
  
  cst = vi(n, 0);
  ans = int(1e9);
  minfre = sz(ids);
  go(0, 0, 0);
  if (ans >= int(1e9)) printf("CRIME TIME\n");
  else printf("%d\n", ans);
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
