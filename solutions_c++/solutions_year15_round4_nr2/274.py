#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <utility>
int currentcase;

using namespace std;

#define ABS(x) (((x) < 0) ? (-(x)) : (x))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))

int n;
double v, x;
double R[100], C[100];
double eps = 0;

double time (double l2) {
  double l1 = 0;
  double min = 0;
  for (int i = 0; i < n; i++) {
    double bound = (R[i]-l2)/C[i];
    if (i == 0) {
      l1 = bound;
    } else {
      l1 = MIN(l1, bound);
    }
    if (-l2 / C[i] < min) {
      min = -l2 / C[i];
    }
  }
  double max = l1;
  while (v*max > v*min+1e-7) {
    double mid = (max + min) / 2;
    if (mid == min || mid == max) break;
    double mu = 0;
    //fprintf(stderr, "%e:\n", mid);
    for (int i = 0; i < n; i++) {
      double cur = (C[i] * mid + l2) / R[i];
      //fprintf(stderr, "%e\n", cur);
      if (cur > 0)
        mu += cur;
    }
    if (mu <= 1) {
      min = mid;
    } else {
      max = mid;
    }
    //fprintf(stderr, "%e %e\n", min, max);
  }
  //fprintf(stderr, "%e %e %e\n", l1, max, l2);
  return max + l2;
}

double unimod(double min, double max) {
  double fmax = time(max);
  double fmin = time(min);
  //if (currentcase != 45) {
    while (true) {
      max = max * 2;
      double old = fmax;
      fmax = time(max);
      if (fmax <= old) break;
    }
    while (true) {
      min = min * 2;
      double old = fmin;
      fmin = time(min);
      if (fmin <= old) break;
    }
  //}
  while (v*ABS(fmax - fmin) > 1e-8) {
    double mid1 = (2*min + max)/3;
    double mid2 = (2*max + min)/3;
    if (mid1 == max || mid1 == min || mid2 == min || mid2 == max) break;
    double fmid1 = time(mid1);
    double fmid2 = time(mid2);
    if (fmid1 > fmid2) {
      max = mid2;
      fmax = fmid2;
    } else {
      min = mid1;
      fmin = fmid1;
    }
    /*fprintf(stderr, "%e %e %e\n", min, max, eps);
    fprintf(stderr, "%e\n", eps);
    fprintf(stderr, "%e\n", max);
    fprintf(stderr, "%e\n", min);*/
    //fprintf(stderr, "%e %e\n", min, max);
  }
  fprintf(stderr, "%e %e\n", min, max);
  return fmin;
}


int main (void) {
  int T;
  scanf("%d", &T);
  for (currentcase = 1; currentcase <= T; ++currentcase) {
    scanf("%d %lf %lf", &n, &v, &x);
    double maxr = 0;
    double maxc = 0;
    double minc = 0;
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf", &R[i], &C[i]);
      R[i] = 1/R[i];
      C[i] /= x;
      if (i == 0) {
        maxr = R[i]; maxc = C[i]; minc = C[i];
      } else {
        maxr = MAX(R[i], maxr);
        maxc = MAX(C[i], maxc);
        minc = MIN(C[i], minc);
      }
    }
    //eps = MIN(1e-8 / ((x/minc + 1) * v), 1e-7);
    fprintf(stderr, "%d\n", currentcase);
    if (minc > 1 || maxc < 1) {
      printf("Case #%d: IMPOSSIBLE\n", currentcase);
    } else {
      printf("Case #%d: %.7lf\n", currentcase, v*unimod(-maxr, maxr));
    }
  }
  return 0;
}
