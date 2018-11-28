#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cassert>
#include <utility>
#include <algorithm>

using namespace std;

const int MAXN = 2013;

typedef long long llint;

struct Point {
  llint x, y;

  Point () { }
  Point (llint x_, llint y_): x(x_), y(y_) { }
  Point operator+(const Point& o) const { return Point(x + o.x, y + o.y); }
  Point operator-(const Point& o) const { return Point(x - o.x, y - o.y); }
  llint operator*(const Point& o) const { return x * o.x + y * o.y; }
  llint operator%(const Point& o) const { return x * o.y - y * o.x; }
  double arg() const { return atan2(y, x); }

  bool operator<(const Point& o) const {
    return y != o.y ? y < o.y : x < o.x;
  }
} p[MAXN], q[MAXN], r[MAXN];

int grahamScan(int n, Point p[], Point ret[]) {
  int sp, tmp;

  if (n < 3) {
    for (int i = 0; i < n; i++) {
      ret[i] = p[i];
    }
    return n;
  }
  sort(p, p + n);
  ret[0] = p[0];
  ret[1] = p[1];
  sp = 2;
  for (int i = 2; i < n; i++) {
    while (sp > 1 && (ret[sp - 1] - ret[sp - 2]) % (p[i] - ret[sp - 2]) > 0) {
      --sp;
    }
    ret[sp++] = p[i];
  }
  tmp = sp;
  ret[sp++] = p[n - 2];
  for (int i = n - 3; i >= 0; i--) {
    while (sp > tmp && (ret[sp - 1] - ret[sp - 2]) % (p[i] - ret[sp - 2]) > 0) {
      --sp;
    }
    ret[sp++] = p[i];
  }

  return sp - 1;
}

llint area(int n, const Point p[]) {
  llint ret = 0;
  for (int i = 0; i < n; ++i) {
    ret += (p[i] - p[0]) % (p[(i + 1) % n] - p[0]);
  }
  return llabs(ret);
}

bool inside(const Point& a, const Point& b, const Point& c) {
  return (a - c) % (b - c) == 0 && (a - c) * (b - c) <= 0;
}

int sgn(llint x) {
  if (x < 0) {
    return -1;
  } else if (x > 0) {
    return 1;
  } else {
    return 0;
  }
}

int decideSide(const Point& p1, const Point& p2, const Point& l1, const Point& l2) {
  return sgn((l1 - l2) % (p1 - l2)) * sgn((l1 - l2) % (p2 - l2));
}

bool intersection(const Point& p1, const Point& p2, const Point& l1, const Point& l2) {
  return decideSide(p1, p2, l1, l2) < 0 && decideSide(l1, l2, p1, p2) < 0;
}

int main() {
  int re, n, t[MAXN];

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%lld%lld", &p[i].x, &p[i].y);
      q[i] = p[i];
      t[i] = i;
    }

    int m = grahamScan(n, q, r);
    llint s = area(m, r);
    // printf("s = %lld\n", s);

    do {
      for (int i = 0; i < n; ++i) {
        q[i] = p[t[i]];
      }
      llint t = area(n, q);
      // printf("%lld\n", t);
      if (2 * t <= s) {
        goto NEXT;
      }
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (j != i && j != (i + 1) % n && inside(q[i], q[(i + 1) % n], q[j])) {
            goto NEXT;
          }
        }
      }
      for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
          if (intersection(q[i], q[(i + 1) % n], q[j], q[(j + 1) % n])) {
            goto NEXT;
          }
        }
      }
      // puts("OK");
      break;
NEXT:
      ;
    } while (next_permutation(t, t + n));

    printf("Case #%d:", ri);
    for (int i = 0; i < n; ++i) {
      printf(" %d", t[i]);
    }
    puts("");
    fflush(stdout);
  }

  return 0;
}
