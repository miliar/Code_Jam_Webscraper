#include <cstdio>
#include <algorithm>

using namespace std;

void solve() {
  long double C, F, X, mini, mini2, elapsed=0., cps=2.;
  scanf("%Lf%Lf%Lf", &C, &F, &X);
  mini2=elapsed+X/cps;
  if (C>=X) {
    printf("%.9Lf\n", mini2);
    return;
  }
  do {
    mini=mini2;
    elapsed+=C/cps;
    cps+=F;
    mini2=elapsed+X/cps;
  } while (mini2<mini);
  printf("%.9Lf\n", mini);
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i=1; i<=n; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
