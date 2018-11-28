#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>
#include <iomanip>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

int n;
int64 p;

void read() {
  cin >> n >> p;
}

pair<int64, int64> add(pair<int64, int64> a, pair<int64, int64> b) {
  return mp(min(a.fs, b.fs), max(a.sc, b.sc));
}

pair<int64, int64> solve(int64 l, int64 r, int64 a, int64 b, int lev, int64 p) {
  if (r <= p)
    return mp((1LL << n) - 1, b);
  if (p < l)
    return mp(a - 1, 0);

  int64 mid = (l + r) >> 1;
  pair<int64, int64> res = solve(l, mid, a, b - (1LL << lev), lev + 1, p);
  res = add(res, solve(mid + 1, r, a + (1LL << lev), b, lev + 1, p));

  return res;
}

pair<int64, int64> solve() {
  pair<int64, int64> res = solve(0, (1LL << n) - 1, 0, (1LL << n) - 1, 0, p - 1);
  return res;
}

int b[110000], c[110000];
bool ans1[110000], ans2[110000];

pair<int64, int64> tupo() {
  int cnt = 1 << n;
  vector<int> p(cnt);
  forn(i, cnt) {
    p[i] = i;
    ans1[i] = true;
    ans2[i] = false;
  }

  do {
    vector<int> a(p);
    forn(i, n) {
      int len = 1 << (n - i);

      for (int j = 0; j < cnt; j += len) {
        forn(t, len / 2) {
          b[t] = a[j + (t << 1)];
          c[t] = a[j + (t << 1 | 1)];
          if (b[t] > c[t])
            swap(b[t], c[t]);
        }
        forn(t, len / 2) {
          a[j + t] = b[t];
          a[j + t + len / 2] = c[t];
        }
      }
    }

    forn(i, ::p)
      ans2[a[i]] = true;
    for (int i = ::p; i < cnt; i++)
      ans1[a[i]] = false;
  } while (next_permutation(all(p)));

  int res1, res2;
  forn(i, cnt) {
    if (ans1[i])
      res1 = i;
    if (ans2[i])
      res2 = i;
  }

  return mp(res1, res2);
}

int main() {
#ifdef RADs_project
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  
  int tt;
  cin >> tt;
  forn(ii, tt) {
    read();
    printf("Case #%d: ", ii + 1);
    //solve();
    pair<int64, int64> res = solve();
    cout << res.fs << ' ' << res.sc << endl;
  }
  
  return 0;
}