#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

int T, N, positives, negtives;
struct point {
  long long x, y;
} p[15];
int res[15];

int main() {
  std::cin >> T;

  for (int n_case = 1; n_case <= T; n_case++) {
    std::cin >> N;
    for (int i = 0; i < N; i++)
      std::cin >> p[i].x >> p[i].y;
    long long a, b, c, v;
    std::fill(res, res+N, 3000);
    for (int i = 0; i < N; i++) {
      for (int j = i+1; j < N; j++) {
        positives = negtives = 0;
        a = p[i].y - p[j].y;
        b = -(p[i].x - p[j].x);
        c = -a*p[i].x - b*p[i].y;
        for (int k = 0; k < N; k++) {
          v = a*p[k].x + b*p[k].y + c;
          if (v > 0) positives++;
          else if (v < 0) negtives++;
        }
        if (positives > negtives) positives = negtives;
        if (res[i] > positives) res[i] = positives;
        if (res[j] > positives) res[j] = positives;
      }
    }

    std::printf ("Case #%d:\n", n_case);
    if (N == 1) res[0] = 0;
    for (int i = 0; i < N; i++)
      std::printf ("%d\n", res[i]);
  }

  return 0;
}
