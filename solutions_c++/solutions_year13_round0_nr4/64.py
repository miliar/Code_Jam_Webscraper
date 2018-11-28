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

int n, have[210], z[2100000], t[210];
vector<int> g[210];

bool rec(int msk) {
  if (msk == (1 << n) - 1)
    return true;
  if (z[msk] != -1)
    return z[msk] == 1;

  bool res = false;
  for (int i = 0; i < n && !res; i++)
    if ((msk & (1 << i)) == 0 && have[t[i]]) {
      forn(j, g[i].size())
        have[g[i][j]]++;
      have[t[i]]--;

      res |= rec(msk | (1 << i));

      forn(j, g[i].size())
        have[g[i][j]]--;
      have[t[i]]++;
    }

  return z[msk] = res;
}

void recwrite(int msk) {
  if (msk == (1 << n) - 1)
    return;

  bool res = false;
  for (int i = 0; i < n && !res; i++)
    if ((msk & (1 << i)) == 0 && have[t[i]]) {
      forn(j, g[i].size())
        have[g[i][j]]++;
      have[t[i]]--;

      if (rec(msk | (1 << i))) {
        printf(" %d", i + 1);
        return recwrite(msk | (1 << i));
      }

      forn(j, g[i].size())
        have[g[i][j]]--;
      have[t[i]]++;
    }

  throw;
}

int main() {
#ifdef RADs_project
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  
  int tt;
  cin >> tt;
  for (int test = 1; test <= tt; test++) {
    printf("Case #%d:", test);
    int k;
    memset(have, 0, sizeof(have));
    cin >> k >> n;
    forn(i, k) {
      int a;
      cin >> a;
      have[a]++;
    }

    forn(i, n) {
      int cnt;
      g[i].clear();
      cin >> t[i] >> cnt;
      forn(j, cnt) {
        int a;
        cin >> a;
        g[i].pb(a);
      }
    }

    memset(z, -1, sizeof(z));
    bool res = rec(0);
    if (!res)
      puts(" IMPOSSIBLE");
    else {
      recwrite(0);
      puts("");
    }
  }
  
  return 0;
}