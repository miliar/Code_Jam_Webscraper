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

int nlen, y, u[3100][3100], us;
double z[3100][3100];

double rec(int tot, int lf, int rg) {
  if (tot == 0)
    return lf > y;
  if (u[lf][rg] == us)
    return z[lf][rg];
  u[lf][rg] = us;

  double res = 0;
  if (lf < nlen - 1 && rg < nlen - 1)
    res = rec(tot - 1, lf + 1, rg) * 0.5 + rec(tot - 1, lf, rg + 1) * 0.5;
  else if (rg == nlen - 1)
    res = rec(tot - 1, lf + 1, rg);
  else
    res = rec(tot - 1, lf, rg + 1);

  return z[lf][rg] = res;
}

double solve() {
  int n, x;
  scanf("%d%d%d", &n, &x, &y);

  int len = 1;

  int sid;
  if (x < 0)
    sid = (y - x) / 2;
  else
    sid = (y + x) / 2;

  if (sid == 0)
    return 1;
  n--;

  for (int id = 1; id <= sid && n > 0; id++) {
    nlen = len + 2;
    int tot = nlen * 2 - 1;

    if (n >= tot) {
      if (id == sid)
        return 1;
      n -= tot;
      len = nlen;
      continue;
    }

    if (id != sid)
      return 0;

    if (x == 0)
      return 0;

    us++;
    return rec(n, 0, 0);
  }

  return 0;
}

int main() {
#ifdef RADs_project
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  
  int tt;
  cin >> tt;
  forn(ii, tt) {
    double res = solve();
    printf("Case #%d: %.10lf\n", ii + 1, res);
  }
  
  return 0;
}