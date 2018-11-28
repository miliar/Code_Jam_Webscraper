#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
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

class Solver {
  vvi es;
  int curver;
  vb was;

  int dfs(int v) {
    if (was[v]) return 0;
    was[v] = true;

    int res = 0;
    if (v > curver) res++;
    for (int i = 0; i < sz(es[v]); i++)
      res += dfs(es[v][i]);
    return res;
  }

  public:
  Solver(int n) : es(n) {}
  void adde(int a, int b) { // val[a] > val[b]
    es[a].pb(b);
  }
  vi solve() {
    const int n = sz(es);
    vi cnts(n);
    for (curver = 0; curver < n; curver++) {
      was = vb(n, false);
      cnts[curver] = dfs(curver);
    }

    vi res(n, -1);
    for (int i = n - 1; i >= 0; i--) {
      int c = cnts[i];

      assert(i + c < n);
      for (int i2 = i + 1; i2 < n; i2++)
        if (res[i2] >= c)
          res[i2]++;
      res[i] = c;
    }
    return res;
  }
};

void solve() {
  int n;
  scanf("%d", &n);
  vi as(n), bs(n);
  for (int i = 0; i < n; i++)
    scanf("%d", &as[i]);
  for (int i = 0; i < n; i++)
    scanf("%d", &bs[i]);

  Solver s(n);
  for (int i = 0; i < n; i++) {
    for (int pr = i - 1; pr >= 0; pr--)
      if (as[pr] == as[i]) {
        s.adde(pr, i);
        break;
      }
    for (int pr = i - 1; pr >= 0; pr--)
      if (as[pr] + 1 == as[i]) {
        s.adde(i, pr);
        break;
      }

    for (int ne = i + 1; ne < n; ne++)
      if (bs[ne] == bs[i]) {
        s.adde(ne, i);
        break;
      }
    for (int ne = i + 1; ne < n; ne++)
      if (bs[ne] + 1 == bs[i]) {
        s.adde(i, ne);
        break;
      }
  }
  vi res = s.solve();
  assert(sz(res) == n);
  for (int i = 0; i < sz(res); i++)
    printf("%d%c", res[i] + 1, "\n "[i + 1 < sz(res)]);

  for (int i = 0; i < n; i++) {
    int cma = 0;
    for (int pr = 0; pr < i; pr++)
      if (res[pr] < res[i])
        cma = max(cma, as[pr]);
    assert(cma + 1 == as[i]);

    cma = 0;
    for (int ne = i + 1; ne < n; ne++)
      if (res[ne] < res[i])
        cma = max(cma, bs[ne]);
    assert(cma + 1 == bs[i]);
  }
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "std";
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
