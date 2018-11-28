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

const int NMAX = 110000;

int v1[NMAX], v2[NMAX], l[NMAX], r[NMAX], id[NMAX], n, m, p, w[NMAX];
bool u[NMAX];
int64 d[1100][1100], dl[1100][1100], d0[NMAX];
vector<pair<int, int> > g[NMAX];

int64 len(int i) {
  if (u[i])
    return l[i];
  else
    return r[i];
}

void read() {
  cin >> n >> m >> p;
  forn(i, m) {
    scanf("%d%d%d%d", &v1[i], &v2[i], &l[i], &r[i]);
    v1[i]--;
    v2[i]--;
  }

  memset(u, 0, sizeof(u));
  forn(i, p) {
    scanf("%d", &id[i]);
    id[i]--;
    u[id[i]] = true;
  }
}

void path(int cnt) {
  forn(i, m)
    w[i] = r[i];

  forn(i, cnt)
    w[id[i]] = l[id[i]];

  forn(i, n)
    g[i].clear();
  forn(i, m)
    g[v1[i]].pb(mp(v2[i], w[i]));

  forn(i, n)
    d0[i] = INF64;
  d0[0] = 0;

  set<pair<int64, int> > q;
  q.insert(mp(0LL, 0));

  while (!q.empty()) {
    int v = q.begin()->sc;
    q.erase(q.begin());

    forn(i, g[v].size()) {
      int to = g[v][i].fs;
      int64 nd = d0[v] + g[v][i].sc;

      if (d0[to] > nd) {
        q.erase(mp(d0[to], to));
        d0[to] = nd;
        q.insert(mp(d0[to], to));
      }
    }
  }
}

void solve() {
  forn(i, n)
    forn(j, n)
      dl[i][j] = d[i][j] = i == j ? 0 : INF64;
  forn(i, m) {
    d[v1[i]][v2[i]] = min(d[v1[i]][v2[i]], len(i));
    dl[v1[i]][v2[i]] = min(dl[v1[i]][v2[i]], (int64)l[i]);
  }

  forn(k, n)
    forn(i, n)
      forn(j, n) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        dl[i][j] = min(dl[i][j], dl[i][k] + dl[k][j]);
      }

  int64 s = 0;
  forn(i, p)
    s += len(id[i]);
  if (d[0][1] == s) {
    puts("Looks Good To Me");
    return;
  }

  int64 sum = 0;
  forn(i, p) {
    sum += len(id[i]);
    int v = v2[id[i]];
    
    path(i + 1);
    
    if (d0[v] < sum) {
      printf("%d\n", id[i] + 1);
      return;
    }

    int64 mi = dl[v][1];

    bool bad = dl[v][1] + sum > d0[1];

    if (bad) {
      printf("%d\n", id[i] + 1);
      return;
    }
  }

  throw;
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