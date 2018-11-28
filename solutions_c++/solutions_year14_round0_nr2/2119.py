#include <cstdio>

double C, F, X;
int y;

void work(int ind) {
  printf("Case #%d: ", ind);
  scanf("%lf %lf %lf", &C, &F, &X);
  double temp = (X / C) - (2 / F) - 1;
  double ans = 0;
  if(temp < 0) {
    ans = X / 2;
    printf("%.8lf\n", ans);
    return;
  }
  y = (int) temp;
  int i;
  double den = 2;

  for(i = 0; i <= y; i++) {
    ans += (C / den);
    den += F;
  }
  ans += (X / den);
  printf("%.8lf\n", ans);
}
  

int main() {
  int T;
  scanf("%d", &T);
  int i;
  for(i = 0; i < T; i++) {
    work(i + 1);
  }
  return 0;
}
