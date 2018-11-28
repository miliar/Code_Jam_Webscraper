#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <list>
#include <iterator>
#include <functional>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pnt;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define FILE ""

const int INF = 1000 * 1000 * 1000 + 5;
const int MOD = 1000 * 1000 * 1000 + 7;
const ld EPS = 1e-9;

int g[5][5] = {{0, 0, 0, 0, 0},
               {0, 1, 2, 3, 4},
               {0, 2, -1, 4, -3},
               {0, 3, -4, -1, 2},
               {0, 4, 3, -2, -1}};

int conv(char c) {
  if (c == '1') {
    return 1;
  }
  if (c == 'i') {
    return 2;
  }
  if (c == 'j') {
    return 3;
  }
  if (c == 'k') {
    return 4;
  }
  assert(false);
}

int f(int x, int y) {
  if (y < 0) {
    x = -x;
    y = -y;
  }
  if (x < 0) {
    return -g[-x][y];
  }
  return g[x][y];
}

int main() {
#ifdef HOME
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#else
  //freopen(FILE ".in", "r", stdin);
  //freopen(FILE ".out", "w", stdout);
#endif
  ios_base::sync_with_stdio(false);
  int ts;
  cin >> ts;
  for (int ti = 0; ti < ts; ++ti) {
    int n, m;
    cin >> n >> m;
    string s, t;
    cin >> t;
    for (int i = 0; i < m; ++i) {
      s += t;
    }
    n *= m;

    int wh = 1;
    for (int i = 0; i < n; ++i) {
      wh = f(wh, conv(s[i]));
    }
    bool ans = false;
    for (int i = 0, x = 1, z = wh; i < n && !ans; ++i) {
      x = f(x, conv(s[i]));
      z = f(-conv(s[i]), z);
      for (int j = i + 1, y = 1, zz = z; j < n && !ans; ++j) {
        y = f(y, conv(s[j]));
        zz = f(-conv(s[j]), zz);
        if (x == 2 && y == 3 && zz == 4) {
          ans = true;
        }
      }
    }
    cout << "Case #" << ti + 1 << ": " << (ans ? "YES" : "NO") << "\n";
  }
  return 0;
}
