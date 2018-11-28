#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("B-result.txt", "w", stdout);
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);

    printf("Case #%d: ", i + 1);

    int n = 0;
    double time_result = 0.0;

    while (true)
    {
      double new_result = time_result + c / (2.0 + f * n);
      double f1 = time_result + x / (2.0 + f * n);
      double f2 = new_result + x / (2.0 + f * (n + 1) );

      if (f1 < f2)
        break;

      ++n;
      time_result = new_result;
    }

    time_result += x / (2.0 + f * n);
    printf("%.8lf", time_result);

    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);

  return 0;
}
