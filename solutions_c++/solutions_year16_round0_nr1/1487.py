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

vi digs(int n) {
  vi d;
  while (n) {
    d.pb(n % 10);
    n /= 10;
  }
  return d;
}

void solve(int n) {
  if  (n == 0) {
    puts("INSOMNIA");
    return;
  }

  vi was(10, false);
  for (int i = 1, cnt_was = 0; cnt_was < 10; ++i) {
    assert(i * 1ll * n <= 1e9);
    for (int d : digs(i * n)) {
      if  (!was[d]) {
        ++cnt_was;
      }
      was[d] = true;
    }
    if  (cnt_was == 10) {
      printf("%d\n", i * n);
      return;
    }
  }
  assert(false);
}

int main() {
#ifdef LOCAL
  freopen(FILE_NAME ".in", "r", stdin);
  freopen(FILE_NAME ".out", "w", stdout);
#endif

  int T;
  scanf("%d\n", &T);
  forn(tt, T) {
    printf("Case #%d: ", tt + 1);
    int n;
    scanf("%d", &n);
    solve(n);
  }

#ifdef LOCAL
  cerr << "Time: " << (double) clock() / CLOCKS_PER_SEC << endl;
#endif
  return 0;
}
