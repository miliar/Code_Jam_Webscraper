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

void solve() {
  int n;
  vi data;
  {
    ll p, q, r, s;
    assert(scanf("%d%I64d%I64d%I64d%I64d", &n, &p, &q, &r, &s) == 5);

    data = vi(n);
    for (int i = 0; i < n; i++) {
      data[i] = ((i * p + q) % r + s);
//      eprintf("data[] = %d\n", data[i]);
    }
  }
  vector<ll> sums(n + 1);
  forn (i, n)
    sums[i + 1] = sums[i] + data[i];

  ll L = -1, R = sums[n];
  while (L + 1 < R) {
    ll M = (L + R) / 2;

    int ptr = 0;
    ll off = 0;
//    eprintf("M=%I64d\n", M);
    for (int k = 0; k < 3 && ptr < n; k++) {
//      eprintf("ptr=%d, off=%I64d\n", ptr, off);
      off = sums[ptr];
      while (ptr < n && sums[ptr + 1] <= off + M) ptr++;
    }
    if (ptr >= n) R = M;
    else L = M;
  }
  printf("%.18lf\n", double(sums[n] - R) / sums[n]);
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
