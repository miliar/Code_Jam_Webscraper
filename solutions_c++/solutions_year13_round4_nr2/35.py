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

bool can(int n, ll id, ll cnt) {
  if (cnt == 0) return false;
  if (cnt >= (1LL << n)) return true;

  assert(0 <= id && id < (1LL << n));
  assert(1 <= cnt && cnt < (1LL << n));

  if (id == 0) return true;
  if (id == (1LL << n) - 1) return false;

  assert(n > 1);
  ll minBadCnt = (id + 1) / 2;
  return can(n - 1, minBadCnt, cnt);
}
bool canNotBeRanked(int n, ll id, ll cnt) {
  return can(n, (1LL << n) - id - 1, (1LL << n) - cnt);
}

void solve() {
  int n; ll p;
  scanf("%d%I64d", &n, &p);

  ll ans1 = -1, ans2 = -1;
  { // Who could win a prize?
    ll L = 0, R = 1LL << n;
    while (L + 1 < R) {
      ll M = (L + R) / 2;
      if (can(n, M, p))
        L = M;
      else
        R = M;
    }
    ans2 = L;

    if (n <= 20) {
      for (int i = 0; i < (1 << n); i++) {
        assert(can(n, i, p) == (i <= ans2));
      }
    }
  }
  { // Who is guaranteed?
    ll L = 0, R = 1LL << n;
    while (L + 1 < R) {
      ll M = (L + R) / 2;
      if (canNotBeRanked(n, M, p))
        R = M;
      else
        L = M;
    }
    ans1 = L;
    if (n <= 20) {
      for (int i = 0; i < (1 << n); i++) {
        assert(canNotBeRanked(n, i, p) == (i > ans1));
      }
    }
  }

  printf("%I64d %I64d\n", ans1, ans2);
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
