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

char buf[11000000];

#define double long double

string s;

void read() {
  cin >> s;
}

double z[2100000];
int u[2100000], us, n;

double rec(int msk) {
  if (msk == (1 << n) - 1)
    return 0;
  if (u[msk] == us)
    return z[msk];

  u[msk] = us;

  double res = 0;
  int cnt = 0;
  forn(i, n) {
    int wait = -1;
    forn(j, n)
      if ((msk & (1 << ((i + j) % n))) == 0) {
        wait = j;
        break;
      }
    if (wait == -1)
      throw;

    res += rec(msk | (1 << ((i + wait) % n))) + n - wait;
  }
  res /= n;

  return z[msk] = res;
}

void solve() {
  n = (int)s.size();

  int msk = 0;
  forn(i, n)
    if (s[i] == 'X')
      msk |= 1 << i;

  us++;

  double res = rec(msk);

  cout.setf(ios::fixed);
  cout.precision(15);
  cout << res << endl;
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