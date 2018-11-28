#include <cstdio>

const double EPS = 1e-8;

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);

    double speed = 2.0;
    double time = 0;
    while (x / speed > c / speed + x / (speed + f) + EPS)
    {
      time += c / speed;
      speed += f;
    }

    time += x / speed;
    printf("Case #%d: %.7lf\n", t + 1, time);
  }

  return 0;
}
