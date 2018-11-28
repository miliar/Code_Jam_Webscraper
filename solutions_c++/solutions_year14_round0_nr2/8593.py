#include <cstdio>
#include <cstdlib>

#define MAXK 100000000

int main()
{
  int T;
  double C, F, X;

  scanf("%d", &T);
  for (int t = 1; t <= T; t++)
    {
      scanf("%lf %lf %lf", &C, &F, &X);

      double mintk = X/2;
      double sum = 0.0;
      for (int k = 1; k < MAXK; k++) {
	sum = sum + 1/(2 + (k-1)*F);
	double tk = X/(2 + k*F) + C*sum;
	if (tk > mintk) {
	  break;
	}
	mintk = tk;
      }

      printf("Case #%d: %.7f\n", t, mintk);
    }

  return EXIT_SUCCESS;
}
