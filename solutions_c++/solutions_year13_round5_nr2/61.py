#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())

typedef long long ll;

typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

int sgn(int x) { return x < 0 ? -1 : x > 0; }
struct pt {
  int x, y;
  pt() : x(0), y(0) {}
  pt(int x, int y) : x(x), y(y) {}
  pt operator-(const pt &p2) const { return pt(x - p2.x, y - p2.y); }
  int operator*(const pt &p2) const { return (x * p2.y - y * p2.x); }
  bool operator==(const pt &p2) const { return x == p2.x && y == p2.y; }
};

bool is_in(int l, int r, int x) {
  if (l > r) swap(l, r);
  return l <= x && x <= r;
}

bool contains_o(pt a, pt b, pt v) {
  if (a == v) return false;
  if (b == v) return false;
  if ((v - a) * (b - a)) return false;
  if (!is_in(a.x, b.x, v.x)) return false;
  if (!is_in(a.y, b.y, v.y)) return false;
  return true;
}

bool contains_h(pt a, pt b, pt v) {
  if (a == v) return true;
  if (a == b) return false;
  return contains_o(a, b, v);
}

// [a1, b1) and [a2, b2)
bool cross(pt a1, pt b1, pt a2, pt b2) {
  if (contains_h(a1, b1, a2)) return true;
  if (contains_h(a2, b2, a1)) return true;

  // (a1, b1) and (a2, b2)
  if ((b1 - a1) * (b2 - a2) == 0) {
    if ((a2 - a1) * (b1 - a1) != 0) return false;
    if ((b2 - a1) * (b1 - a1) != 0) return false;
    swap(a1, a2);
    swap(b1, b2);
    if ((a2 - a1) * (b1 - a1) != 0) return false;
    if ((b2 - a1) * (b1 - a1) != 0) return false;

    if (contains_o(a1, b1, a2)) return true;
    if (contains_o(a1, b1, b2)) return true;
    swap(a1, a2);
    swap(b1, b2);
    if (contains_o(a1, b1, a2)) return true;
    if (contains_o(a1, b1, b2)) return true;
    return false;
  } else {
    if ( sgn((a2 - a1) * (b1 - a1)) * sgn((b2 - a1) * (b1 - a1)) >= 0) return false;
    swap(a1, a2);
    swap(b1, b2);
    if ( sgn((a2 - a1) * (b1 - a1)) * sgn((b2 - a1) * (b1 - a1)) >= 0) return false;
    return true;
  }
  assert(false);
}

void solve() {
  int n;
  scanf("%d", &n);
  vector<pt> pts0(n);
  for (int i = 0; i < n; i++)
    scanf("%d%d", &pts0[i].x, &pts0[i].y);

  double ans = -1;
  vi aord;

  vi ord(n);
  for (int i = 0; i < n; i++)
    ord[i] = i;

  do {
    vector<pt> pts(n);
    for (int i = 0; i < n; i++)
      pts[i] = pts0[ord[i]];
    pts.pb(pts[0]);

    bool g = true;
//    assert(!cross(pts[1], pts[2], pts[3], pts[4]));
    for (int a = 0; a < n; a++) {
      for (int b = a + 1; b < n; b++) {
        if (cross(pts[a], pts[a + 1], pts[b], pts[b + 1])) {
          g = false;
          goto end;
//          eprintf("%d %d\n", a, b);
        }
      }
    }
    end:;
//    exit(0);
    if (g) {
      int sum = 0;
      for (int i = 0; i < n; i++)
        sum += pts[i] * pts[i + 1];
      sum = abs(sum);
      if (sum > ans) {
        ans = sum;
        aord = ord;
      }
    }
  } while (next_permutation(ord.begin(), ord.end()));

  assert(sz(aord) == n);
  for (int i = 0; i < n; i++)
    printf("%d%c", aord[i], "\n "[i + 1 < n]);
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "";
    if (argc >= 2) fn = argv[1];
    if (endsWith(fn, ".in")) fn = string(fn, 0, fn.length() - 3);
    freopen((fn + ".in").c_str(), "r", stdin);
    freopen((fn + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    eprintf("Case #%d:\n", TN);
    printf("Case #%d: ", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Catched exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
