#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <cstdlib>
#include <memory>
#include <queue>
#include <cassert>
#include <cmath>
#include <ctime>
#include <complex>
#include <bitset>
#include <fstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define pb push_back
#define fst first
#define snd second
#define mp make_pair 
#define sz(C) ((int) (C).size())
#define forn(i, n) for (int i = 0; i < (int) n; ++i)
#define ford(i, n) for (int i = ((int) n) - 1; i >= 0; --i)
#define y1 gftxdtrtfhyjfctrxujkvbhyjice
#define y0 ehfoiuvhefroerferjhfjkehfjke
#define left sdhfsjkshdjkfsdfgkqqweqweh
#define right yytrwtretywretwreytwreytwr
#define next jskdfksdhfjkdsjksdjkgf
#define prev koeuigrihjdkjdfj
#define hash kjfdkljkdhgjdkfhgurehg
#define all(C) begin(C), end(C)

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vector <int> > vvi;
typedef vector<pii> vii;
typedef long double ld;
typedef complex<double> cd;
typedef vector<cd> vcd;

#define FILE_NAME ""

void go(int i, int n, uint mask, int c0, int c1, int need, vvi& res) {
  if  (sz(res) >= need) {
    return;
  }

  if  (i == n && c0 == c1) {
    vi cur;
    cur.pb(mask);
    forn(i, 9) cur.pb(i + 3);
    res.pb(cur);
    return;    
  }

  if  (i == n) {
    return;
  }

  int rest = n - i;
  if  (rest < abs(c0 - c1)) {
    return;
  }

  if  (i != 0 && i != n - 1) {
    go(i + 1, n, mask, c0, c1, need, res);
  }

  if  (i & 1) {
    ++c1;
  } else {
    ++c0;
  }
  go(i + 1, n, mask | (1u << i), c0, c1, need, res);
}

vvi solve(int n, int j) {
  vvi res;
  go(0, n, 0, 0, 0, j, res);
  return res;
}

bool check(const vi& c, int n) {
  for (int i = 1; i < sz(c); ++i) {
    int base = i + 1;
    int mod = c[i];
    uint mask = c[0];
    int num = 0;
    ford(j, n) {
      num = (num * base) % mod;
      if  (mask & (1u << j)) {
        num = (num + 1) % mod;
      }
    }
    if  (num != 0) {
      return false;
    }
  }
  return true;
}

bool check(const vvi& res, int n) {
  for (const auto& cur : res) {
    if  (!check(cur, n)) {
      return false;
    }
  }
  return true;
}

int main() {
#ifdef LOCAL
  freopen(FILE_NAME ".in", "r", stdin);
  freopen(FILE_NAME ".out", "w", stdout);
#endif

  int T;
  scanf("%d", &T);
  assert(T == 1);
  
  
  int n, j;
  scanf("%d%d", &n, &j);
  auto res = solve(n, j);
  assert(check(res, n));
  printf("Case #1:\n");
  for (const auto& cur : res) {
    uint mask = cur[0];
    ford(i, n) {
      printf("%d", (mask >> i) & 1);
    }
    printf(" ");
    for (int i = 1; i < sz(cur); ++i) {
      printf("%d ", cur[i]);
    }
    puts("");
  } 

#ifdef LOCAL
  cerr << "Time: " << (double) clock() / CLOCKS_PER_SEC << endl;
#endif
  return 0;
}
