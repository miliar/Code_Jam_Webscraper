#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

#define MAXN 1005
#define EPS 1e-8

int p[MAXN];

int main() {
  int T;
  scanf("%d", &T);
  for (int nCase = 1; nCase <= T; ++nCase) {
    int D;
    scanf("%d", &D);
    int pmax = 0;
    for (int i = 0; i < D; ++i) {
      scanf("%d", p + i);
      pmax = max(pmax, p[i]);
    }
    int ret = pmax;
    for (int i = 1; i <= pmax; ++i) {
      // base at i
      int tot = i;
      for (int j = 0; j < D; ++j) {
        tot += (p[j] - 1) / i;
      }
      ret = min(ret, tot);
    }
    printf("Case #%d: %d\n", nCase, ret);
  }
  return 0;
}

