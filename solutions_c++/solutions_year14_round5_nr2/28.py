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

int dd, dt, n;
vi hs, gs;

const int MAXN = 105;
const int MAXH = 205;
const int MAXRES = 1005;
int cache[MAXN][MAXH + 1][MAXRES + 1][2];

int calc(int pos, int remh, int reserve, int turn) {
  if (pos >= n) return 0;

  assert(0 <= pos && pos < n);
  assert(0 < remh && remh <= MAXH);
  assert(0 <= reserve && reserve <= MAXRES);
  assert(turn == !!turn);
  int &ans = cache[pos][remh][reserve][turn];
  if (ans >= 0) return ans;

  assert(remh > 0);
  if (turn == 1) {
    remh -= dt;
    if (remh > 0) return ans = calc(pos, remh, reserve + 1, 0);
    else return ans = calc(pos + 1, hs[pos + 1], reserve + 1, 0);
  }

  ans = calc(pos, remh, reserve, 1);
  if (reserve > 0) {
    remh -= dd;
    int cans;
    if (remh > 0) {
      cans = calc(pos, remh, reserve - 1, 0);
    } else {
      cans = calc(pos + 1, hs[pos + 1], reserve - 1, 0) + gs[pos];
    }
    ans = max(ans, cans);
  }
  return ans;
}

void solve() {
  scanf("%d%d%d", &dd, &dt, &n);

  hs = vi(n);
  gs = vi(n);
  forn (i, n)
    scanf("%d%d", &hs[i], &gs[i]);
  hs.pb(0);
  gs.pb(-1);

  memset(cache, -1, sizeof cache);
  int ans = 0;
  ans = max(ans, calc(0, hs[0], 1, 0));
  printf("%d\n", ans);
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
