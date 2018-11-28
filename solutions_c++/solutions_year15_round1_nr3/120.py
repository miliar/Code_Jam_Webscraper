#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int MAXN = 3000 + 10;
struct Point {
  LL x, y;
  Point() {}
  Point(LL x, LL y): x(x), y(y) {}
  bool operator < (const Point &rhs) const {
    return x < rhs.x || (x == rhs.x && y < rhs.y);
  }
  Point operator + (const Point &rhs) const {
    return Point(x + rhs.x, y + rhs.y);
  }
  Point operator - (const Point &rhs) const {
    return Point(x - rhs.x, y - rhs.y);
  }
  LL dot(const Point &rhs) const {
    return x * rhs.x + y * rhs.y;
  }
  LL det(const Point &rhs) const {
    return x * rhs.y - y * rhs.x;
  }
};

Point P[MAXN];
int N, ret[MAXN]; 

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    scanf("%d", &N);
    for (int i = 0; i < N; ++ i) {
      scanf("%lld%lld", &P[i].x, &P[i].y);
      ret[i] = N - 1;
    }
    for (int i = 0; i < N; ++ i) {
      for (int j = 0; j < N; ++ j) if (i != j) {
        int same = 0, left = 0;
        Point A = P[j] - P[i];
        for (int k = 0; k < N; ++ k) {
          LL v = A.det(P[k] - P[i]);
          if (v == 0) same ++;
          else if (v > 0) left ++;
        }
        ret[i] = min(ret[i], N - same - left);
        ret[j] = min(ret[j], N - same - left);
      }
    }
    printf("Case #%d:\n", cas);
    for (int i = 0; i < N; ++ i) printf("%d\n", ret[i]);
  }
  return 0;
}
