#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

#define Nmax (1<<10)
#define mp make_pair

int d, t;
int P[Nmax];

bool solve(int k) {
  // brute force
  for (int dmin = k; dmin >= 1; --dmin) {
    int pause = 0;
    for (int i = 1; i <= d; ++i) {
      if (P[i] <= dmin)
        continue;
      int buckets = (P[i] + (dmin - 1)) / dmin;
      pause += buckets - 1;
    }

    //printf ("%d %d %d %d\n", d, pause, dmin, k);
    if (pause + dmin <= k)
      return true;
  }
  return false;
}

int main() {
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {

    scanf("%d", &d);
    for (int i = 1; i <= d; ++i) {
      scanf("%d", &P[i]);
    }
    
    int m, step;
    for (step = 1; step <= Nmax; step <<= 1);
    for (m = Nmax; step; step >>= 1)
      if ( solve(m - step) )
        m -= step;
   
    printf("Case #%d: %d\n", ti, m);
  }
}
