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

const int MOD = 1000002013;
void madd(int &a, int b) { if ((a += b) >= MOD) a -= MOD; }
int mmul(int a, int b) { return ll(a) * b % MOD; }

int n;
int calc(int len) {
  int res = mmul(n, len);
  int a = len, b = len - 1;
  if (a & 1) b >>= 1;
  else a >>= 1;
  madd(res, MOD - mmul(a, b));
  return res;
}

void solve() {
  int m;
  scanf("%d%d", &n, &m);

  int base = 0;
  map<int, ll> bal;
  for (int i = 0; i < m; i++) {
    int st, en, cnt;
    scanf("%d%d%d", &st, &en, &cnt);
    assert(0 <= cnt && cnt <= (int)1e9);
    madd(base, mmul(calc(en - st), cnt));
    bal[st] += cnt;
    bal[en] -= cnt;
  }
  vector<pair<int, ll> > as;
  for (map<int, ll>::iterator it = bal.begin(); it != bal.end(); it++)
    if (it->second)
      as.pb(*it);

  eprintf("base=%d, sz=%d\n", base, sz(as));
  vector<pair<int, ll> > curStack;
  int ans = 0;
  for (int i = 0; i < sz(as); i++) {
    if (as[i].second > 0) {
      curStack.pb(as[i]);
      continue;
    }
    ll rem = -as[i].second;
    while (rem > 0) {
      assert(!curStack.empty());
      ll cnt = min(rem, curStack.back().second);
      madd(ans, mmul(calc(as[i].first - curStack.back().first), cnt % MOD));
      rem -= cnt;
      if ((curStack.back().second -= cnt) == 0)
        curStack.pop_back();
    }
    assert(rem == 0);
  }
  assert(curStack.empty());

  madd(base, MOD - ans);
  printf("%d\n", base);
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
