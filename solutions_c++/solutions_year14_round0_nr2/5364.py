#include <stdio.h>

#define EPS 1e-9

int T;
long double C, F, X;
long double P;
long double time;
long double t1, t2;

int main() {
  
  scanf("%d", &T);
  int c = 0;
  while (T--) {
    c++;
    scanf("%Lf %Lf %Lf", &C, &F, &X);
    
    P = 2;
    time = 0;
    while (true) {
      t1 = X / P;
      t2 = C / P + X / (P + F);
      if (t1 < t2 - EPS) {
	time = time + t1;      
	break; 
      }
      time = time + C/P;
      P += F;
    }  
    
    printf("Case #%d: %.7Lf\n", c, time);
  }
  
  return 0;
}