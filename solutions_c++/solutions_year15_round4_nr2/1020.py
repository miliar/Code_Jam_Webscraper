#include <memory.h>
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef int64_t i64;
template <size_t size>
using ai = array<int, size>;
template <size_t height, size_t width>
using aai = array<ai<width>, height>;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;

struct Water {
  double R;
  double C;
};

inline bool IsSame(double a, double b) {
  return abs(a - b) <= 0.000001;
}

int main() {
  int T = 0;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    int N = 0;
    double V = 0.0;
    double X = 0.0;
    scanf("%d %lf %lf", &N, &V, &X);

    static array<Water, 110> waters;
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &waters[i].R, &waters[i].C);
    }

    printf("Case #%d: ", tt);

    if (N == 1) {
      if (IsSame(waters[0].C, X)) {
        printf("%.10lf\n", V / waters[0].R);
      } else {
        printf("IMPOSSIBLE\n");
      }
    } else {
      bool impossible = false;
      double answer = 0.0;
      double one_sec = (waters[0].R * waters[0].C + waters[1].R * waters[1].C) / (waters[0].R + waters[1].R);
      if (IsSame(one_sec, X)) {
        answer = V / (waters[0].R + waters[1].R);
      } else {
        if (IsSame(waters[0].C, X)) {
          answer = V / waters[0].R;
        } else if (IsSame(waters[1].C, X)) {
          answer = V / waters[1].R;
        } else if (min(waters[0].C, waters[1].C) <= X && max(waters[0].C, waters[1].C) >= X) {
          double k_sec = waters[0].R * (waters[0].C - X) / (waters[1].R * (X - waters[1].C));
          answer = max(k_sec, 1.0) * V / (waters[0].R + k_sec * waters[1].R);
        } else {
          impossible = true;
        }
      }

      if (impossible) {
        printf("IMPOSSIBLE\n");
      } else {
        printf("%.10lf\n", answer);
      }
    }
  }

  return 0;
}
