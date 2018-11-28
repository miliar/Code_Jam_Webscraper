#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <utility>

using namespace std;

char s[205];

double dp[21][1 << 20];
int n;
double n_inv;

double get (int x) {
  if (x == 0) {
    return 0;
  }
  double &res = dp[n][x];
  if (res > 0) {
    return res;
  }
  for (int i = 0; i < n; i++) {
    if (((x >> i) & 1)) {
      int j;
      int k = 1;
      for (j = i - 1; j >= 0 && ((x >> j) & 1) == 0; j--) {
        k++;
      }
      if (j == -1) {
        for (j = n - 1; ((x >> j) & 1) == 0; j--) {
          k++;
        }
      }
      res += k * (k - 1) * 0.5 + k * get (x - (1 << i));
    }
  }
  res *= n_inv;
  return res;
}



int main (void) {
  int tn, nt;
  scanf ("%d\n", &nt);

  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    gets (s);
    n = strlen (s);
    n_inv = 1.0 / n;
    int x = 0;
    int r = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == '.') {
        x += (1 << i);
        r++;
      }
    }
    printf ("%.10lf\n", r * n - get (x));
  }

  return 0;
}
