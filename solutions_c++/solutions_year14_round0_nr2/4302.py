#include <cstdio>

using namespace std;

int main()
{
  int T;
  double lambda=2;
  
  scanf("%d", &T);
  for(int i=0; i<T; i++) {
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);

    double tk=0, Tmin=1e5;
    for(int k=0; 1; k++) {
      if(tk+X/(lambda+k*F)<Tmin)
	Tmin = tk+X/(lambda+k*F);
      else
	break;
      tk += C/(lambda+k*F);
    }
    printf("Case #%d: %.7lf\n", i+1, Tmin);
  }

  return 0;
}
