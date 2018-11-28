#include <stdio.h>

void solve_case()
{
  double C, F, X, speed = 2, time = 0;
  scanf("%lf %lf %lf", &C, &F, &X);
  while (X/speed > ((C/speed) + (X/(speed+F))))
    {
      time += C/speed;
      speed += F;
    }
  time += X/speed;
  printf ("%.7lf\n", time);
}

int main()
{
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; i++)
    {
      printf ("Case #%d:", i+1);
      solve_case();
    }
  return 0;
}
