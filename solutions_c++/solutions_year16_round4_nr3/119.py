#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <cmath>
#include <queue>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; }
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; }
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

const int EAST = 0;
const int NORTH = 1;
const int WEST = 2;
const int SOUTH = 3;

int dir[4][2] = {
  {0, 1},
  {-1, 0},
  {0, -1},
  {1, 0}
};

struct maze {
  int r, c;
  vector<string> b;

  maze(int r, int c): r(r), c(c) {
    b.resize(3 * r);
    fill(all(b), string(3 * c, '.'));
    FOR(i, 0, r) {
      FOR(j, 0, c) {
        b[i * 3 + 1][j * 3 + 1] = '#';
      }
    }
  }

  pii entry(int index) {
    if (index < c) {
      return pii(0, 3 * index + 1);
    } else {
      index -= c;
    }
    if (index < r) {
      return pii(3 * index + 1, 3 * c - 1);
    } else {
      index -= r;
    }
    if (index < c) {
      return pii(3 * r - 1, 3 * (c - 1 - index) + 1);
    } else {
      index -= c;
    }
    if (index < r) {
      return pii(3 * (r - 1 - index) + 1, 0);
    } else {
      assert(0);
    }
  }

  bool empty(pii p) {
    if (p.first < 0 || p.first >= b.size() || p.second < 0 || p.second >= b[p.first].size()) {
      return false;
    }
    return b[p.first][p.second] != '#';
  }

  pii next(pii p, int d) {
    return pii(p.first + dir[d][0], p.second + dir[d][1]);
  }

  pii left(pii p, int d) {
    return next(p, (d + 1) % 4);
  }

  pii middle(int i, int j) {
    return pii(i * 3 + 1, j * 3 + 1);
  }

  vector<pii> shortest_path(pii u, pii v) {
    vector<pii> path;
    path.pb(u);
    int d = initial_direction(u);
    // cout << "inidi " << d << endl;
    while (path.back() != v) {
      if (Size(path) > 1 && path.back() == u && d == initial_direction(u)) {
        return vector<pii>();
      }
      pii me = path.back();
      if (empty(next(me, d))) {
        path.pb(me = next(me, d));
        if (empty(left(me, d))) {
          d = (d + 1) % 4;
        }
      } else {
        d = (d + 3) % 4;
      }
    }
    return path;
  }

  int initial_direction(pii p) {
    if (p.first == 0) return EAST;
    if (p.first == 3 * r - 1) return WEST;
    if (p.second == 0) return NORTH;
    if (p.second == 3 * c - 1) return SOUTH;
    assert(0);
  }

  // vector<pii> shortest_path(pii u, pii v) {
  //   int r = b.size();
  //   int c = b[0].size();
  //   int d[r][c];
  //   vector<vector<pii> > parent(r, vector<pii>(c));
  //   FOR(i, 0, r) {
  //     FOR(j, 0, c) {
  //       d[i][j] = -1;
  //     }
  //   }
  //   vector<pii> q(r * c);
  //   int head = 0;
  //   int tail = 0;
  //   q[tail++] = u;
  //   d[u.first][u.second] = 0;
  //   while (head < tail) {
  //     pii current = q[head++];
  //     FOR(di, 0, 4) {
  //       pii next(current.first + dir[di][0], current.second + dir[di][1]);
  //       if (next.first < 0 || next.first >= r || next.second < 0 || next.second >= c) {
  //         continue;
  //       }
  //       if (d[next.first][next.second] != -1) {
  //         continue;
  //       }
  //       if (b[next.first][next.second] == '#') {
  //         continue;
  //       }
  //       d[next.first][next.second] = d[current.first][current.second] + 1;
  //       parent[next.first][next.second] = current;
  //       q[tail++] = next;
  //     }
  //   }
  //   if (d[v.first][v.second] == -1) {
  //     return vector<pii>();
  //   }
  //   vector<pii> result;
  //   while (u != v) {
  //     result.pb(v);
  //     v = parent[v.first][v.second];
  //   }
  //   result.pb(u);
  //   return result;
  // }

  void set(pii cell) {
    pii mid = middle(cell.first / 3, cell.second / 3);
    if (mid == pii(cell.first + 1, cell.second + 1) || mid == pii(cell.first - 1, cell.second - 1)) {
      b[mid.first + 1][mid.second - 1] = '#';
      b[mid.first - 1][mid.second + 1] = '#';
    }
    if (mid == pii(cell.first - 1, cell.second + 1) || mid == pii(cell.first + 1, cell.second - 1)) {
      b[mid.first + 1][mid.second + 1] = '#';
      b[mid.first - 1][mid.second - 1] = '#';
    }
  }

  void print() {
    FOR(i, 0, Size(b)) {
      FOR(j, 0, Size(b[i])) {
        cout << b[i][j];
      }
      cout << endl;
    }
  }

  char get(int i, int j) {
    i = 3 * i + 1;
    j = 3 * j + 1;
    if (b[i - 1][j - 1] == '#' || b[i + 1][j + 1] == '#') {
      return '\\';
    }
    if (b[i - 1][j + 1] == '#' || b[i + 1][j - 1] == '#') {
      return '/';
    }
    return '/';
  }
};

void solve() {
  int r, c;
  cin >> r >> c;
  maze m(r, c);
  vector<pii> pairs;
  int counter[2 * (r + c)];
  vector<bool> matched(2 * (r + c), false);
  FOR(i, 0, r + c) {
    int x, y;
    cin >> x >> y;
    x--;
    y--;
    counter[x] = y;
    counter[y] = x;
  }
  FOR(rep, 0, r + c) {
    FOR(i, 0, 2 * (r + c)) {
      pii p(i, counter[i]);
      if (matched[i]) {
        continue;
      }
      bool ok = true;
      for (int index = (p.first + 1) % Size(matched); index != p.second; index = (index + 1) % Size(matched)) {
        if (!matched[index]) {
          ok = false;
        }
      }
      if (!ok) {
        continue;
      }
      // cout << "matching " << p.first << " " << p.second << endl;
      vector<pii> v = m.shortest_path(m.entry(p.first), m.entry(p.second));
      if (v.empty()) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
      FOREACH(it, v) {
        pii cell = *it;
        m.b[cell.first][cell.second] = '@';
        m.set(cell);
      }
      matched[p.first] = matched[p.second] = true;
      // m.print();
    }
  }
  FOR(i, 0, 2 * (r + c)) {
    if (!matched[i]) {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  // cout << endl;
  FOR(i, 0, r) {
    FOR(j, 0, c) {
      cout << m.get(i, j);
    }
    cout << endl;
  }
  // m.print();
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    cout << "Case #" << test_number << ":" << endl;
    solve();
  }
	return 0;
}
