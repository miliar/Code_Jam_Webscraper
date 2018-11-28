#include <cstdio>
#include <algorithm>

#define BIG_NUMBER 6000000

void docase(int tcase) {
  double c, f, x;
  scanf("%lf %lf %lf", &c, &f, &x);

  double min = x / 2;
  double cur = 0;
  for (int i = 0; i < BIG_NUMBER; i++)
  {
    cur += c / (2 + i * f);

    double nx = cur + x / (2 + (i+1)*f);
    if (nx < min)
      min = nx;
  }

  printf("Case #%d: %.7lf\n", tcase, min);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; i++) docase(i+1);
}
