#include <stdio.h>

int main()
{
  int n_cases;
  scanf("%d", &n_cases);
  for (int T = 0; T < n_cases; ++T)
  {
    printf("Case #%d: ", T + 1);
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);
//    fprintf(stderr, "c = %f, f = %f, x = %f\n", c, f, x);
    int n = (f * x - 2 * c) / (c * f);
    if (n < 0) n = 0;
//    fprintf(stderr, "n = %d\n", n);
    double cost = 0;
    for (int i = 0; i < n; ++i)
      cost += c / (2 + i * f);
    cost += x / (2 + n * f);
    printf("%.7f\n", cost);
  }
}
