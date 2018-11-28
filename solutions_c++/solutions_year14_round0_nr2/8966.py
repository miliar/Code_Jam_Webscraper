#include <cstdio>
#include <limits>

using namespace std;

double computeTime (double C, double F, double X, double N) {
  double acum = 0;
  double den = 2.0;
  for (int i = 0; i < N; ++i) {
    acum = acum + C / den;
    den += F;
  }
  acum = acum + X / den;
  return acum;
}

int main () {

  int T;
  scanf ("%d", &T);
 
  for (int k = 1; k <= T; ++k) {
    double C, F, X;
    scanf ("%lf%lf%lf", &C, &F, &X);

    double told = numeric_limits<double>::infinity();
    double t = told;
    for (int i = 0; true; ++i) {
      t = computeTime (C, F, X, i);
      if (t < told)
	told = t;
      else
	break;
    }
    
    printf ("Case #%d: %.7lf\n", k, told);
  }
  return 0;
}
