#include <iostream>
#include <cstdio>
#include <memory.h>
#define MIN(a,b) ((a) < (b) ? (a) : (b))
using namespace std;

const int maxn = 5;
double c,f,x;

void solve() {
  double sum = 0.0, v = 2.0, pre;
  double ans = x / v;
  while(true) {
    sum += (c / v);
    v += f;
    double tmp = sum + x / v;
    if (tmp < ans) ans = tmp;
    else break;
  }
  printf("%.7f\n", ans);
  return;
}

int main() {
  //freopen("data.in", "r", stdin);
  //freopen("B-small-attempt0.in", "r", stdin);
  //freopen("B-large.in", "r", stdin);
  //freopen("data.out", "w", stdout);
  int cas;
  scanf("%d",&cas);
  for (int i=1;i<=cas;i++) {
    printf("Case #%d: ", i);
    scanf("%lf%lf%lf",&c,&f,&x);
    solve();
  }
  return 0;
}
