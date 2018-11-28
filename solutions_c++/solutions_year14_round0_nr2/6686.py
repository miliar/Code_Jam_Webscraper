#include <cstdio>

int main()
{
  int T, t;
  double total, rate, c, f, x;
  
  scanf("%d", &T);
  for (t = 1; t <= T; ++t)
  {
    total = 0.0;
    rate = 2.0;
    
    scanf("%lf %lf %lf", &c, &f, &x);
    while (x / rate > c / rate + x / (rate + f))
    {
      total += c / rate;
      rate += f;
    }
    total += x / rate;
    
    printf("Case #%d: ", t);
    printf("%.7lf\n", total);
  }
  
  return 0;
}
