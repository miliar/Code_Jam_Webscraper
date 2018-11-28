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

#define double long double

char buf[11000000];

const int N = 37;

int64 a[N], b, c[N];

void read() {
  int cnt;
  cin >> b >> cnt;
  forn(i, N)
    a[i] = 0;
  forn(i, cnt)
    cin >> a[i];
}

double calc(int cnt, int64 r) {
  double cur = - (b - r);
  forn(i, cnt)
    cur += 36.0 / cnt * (a[i] - c[i]);
  return cur;
}

void solve() {
  sort(a, a + N);
  memcpy(c, a, sizeof(a));

  double ans = 0;
  for (int cnt = 1; cnt <= N; cnt++) {
    memcpy(a, c, sizeof(c));
    int64 r = b;
    int64 to = a[cnt - 1];
    forn(i, cnt) {
      r -= to - a[i];
      a[i] = to;
      if (r < 0)
        break;
    }

    if (r < 0)
      continue;

    for (int i = cnt; i < N; i++)
      if (a[i] == to) {
        a[i]++;
        r--;
      }

    if (r < 0)
      continue;

    while (r >= 0) {
      ans = max(ans, calc(cnt, r));

      int64 add = r / cnt;
      if (add == 0)
        break;
      if (cnt < N && add >= a[cnt] - a[0])
        add = a[cnt] - a[0] - 1;

      if (add == 0) {
        int k = 0;
        for (int i = cnt; i < N; i++)
          if (a[i] == a[0] + 1)
            k++;

        add = r / (cnt + k);

        if (add == 0)
          break;

        for (int i = cnt; i < N; i++)
          if (a[i] > a[0] + 1)
            add = min(add, a[i] - a[0] - 1);

        int64 a01 = a[0] + 1;

        forn(i, N) 
          if (i < cnt || a[i] == a01) {
            a[i] += add;
            r -= add;
          }
      } else {
        forn(i, cnt) {
          a[i] += add;
          r -= add;
        }
      }
    }
  }

  cout.setf(ios::fixed);
  cout.precision(10);
  cout << ans << endl;
}

int main() {
#ifdef RADs_project
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  
  int tests;
  scanf("%d", &tests);
  gets(buf);

  for (int test = 1; test <= tests; test++) {
    cerr << "Test " << test << " of " << tests << ": " << clock() << endl;

    cout << "Case #" << test << ": ";

    read();
    //gen();
    solve();
  }

  cerr << "Total time: " << clock() << endl;
  
  return 0;
}