#define PRETEST
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <iomanip>
#include <sstream>
using namespace std;

#define INF 0x4f4f4f4f
#define FILL(a,b) memset(a,b,sizeof(a))
#define SQR(a) ((a) * (a))

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef map<string, int> msi;
typedef map<int, int> mii;

const double EPS = 1e-9;

double r[110];
double c[110];

int sign(double x) {
  if (fabs(x) < EPS) {
    return 0;
  }
  return (x > EPS) ? 1 : -1;
}

int main(int argc, char *argv[]) {
#ifdef PRETEST
  freopen("B-small.in", "r", stdin);
#endif
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    int N;
    double V, X;
    scanf("%d%lf%lf", &N, &V, &X);
    for (int i = 0; i < N; ++i) {
      scanf("%lf%lf", r + i, c + i);
    }
    printf("Case #%d: ", cas);
    if (N == 2) {
      if (sign(c[0] - X) < 0 && sign(c[1] - X) < 0) {
        printf("IMPOSSIBLE\n");
        continue;
      }
      if (sign(c[0] - c[1]) == 0) {
        if (sign(c[0] - X) == 0) {
          printf("%.10lf\n", V / (r[0] + r[1]));
        } else {
          printf("IMPOSSIBLE\n");
        }
        continue;
      }
      double t0 = (X - c[1]) * V / (r[0] * (c[0]-c[1]));
      double t1 = (V - r[0] * t0) / r[1];
      if (sign(t0) < 0 || sign(t1) < 0) {
        printf("IMPOSSIBLE\n");
        continue;
      }
      printf("%.10lf\n", max(t0, t1));
    } else if (N == 1) {
      if (sign(c[0] - X) == 0) {
        printf("%.10lf\n", V / r[0]);
      } else {
        printf("IMPOSSIBLE\n");
      }
    }
  }
  return 0;
}

