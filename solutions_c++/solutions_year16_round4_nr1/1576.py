#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

map <vector <int>, string> f;

string getF(int n, int r, int p, int s, int w) {
  if (n == 0) {
    if (w == 0) {
      if (r == 1) {
        return "R";
      } else {
        return "IMPOSSIBLE";
      }
    } else if (w == 1) {
      if (p == 1) {
        return "P";
      } else {
        return "IMPOSSIBLE";
      }
    } else if (w == 2) {
      if (s == 1) {
        return "S";
      } else {
        return "IMPOSSIBLE";
      }
    }
  }
  vector <int> x(4);
  x[0] = r;
  x[1] = p;
  x[2] = s;
  x[3] = w;
  if (f.count(x) > 0) {
    return f[x];
  }
  string res("IMPOSSIBLE");
  for (int r1 = 0; r1 <= r; ++r1) {
    for (int p1 = 0; p1 <= p; ++p1) {
      int s1 = (1 << (n - 1)) - r1 - p1;
      if (s1 < 0 || s1 > s) {
        continue;
      }
      int r2 = r - r1;
      int p2 = p - p1;
      int s2 = s - s1;
      for (int i1 = 0; i1 < 3; ++i1) {
        for (int i2 = 0; i2 < 3; ++i2) {
          if (!((i1 == w && i2 == (w + 2) % 3) || (i2 == w && i1 == (w + 2) % 3))) {
            continue;
          }
          string t1 = getF(n - 1, r1, p1, s1, i1);
          if (t1 == "IMPOSSIBLE") {
            continue;
          }
          string t2 = getF(n - 1, r2, p2, s2, i2);
          if (t2 == "IMPOSSIBLE") {
            continue;
          }
          string t = t1 + t2;
          if (res == "IMPOSSIBLE" || t < res) {
            res = t;
          }
        }
      }
    }
  }
  return f[x] = res;
}

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; ++tt) {
    int n, r, p, s;
    assert(scanf("%d%d%d%d", &n, &r, &p, &s) == 4);
    string res("IMPOSSIBLE");
    for (int i = 0; i < 3; ++i) {
      string t = getF(n, r, p, s, i);
      if (t == string("IMPOSSIBLE")) {
        continue;
      }
      if (res == string("IMPOSSIBLE") || res > t) {
        res = t;
      }
    }
    printf("Case #%d: %s\n", tt, res.c_str());
  }
  return 0;
}
