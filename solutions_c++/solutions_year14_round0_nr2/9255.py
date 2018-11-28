#include<cstdio>

using namespace std;

int main() {
  int T, iteration = 0;
  double C, F, X;
  double oldTime;
  double newTime;
  double R;
  scanf("%d", &T);
  while(T--) {
    iteration++;
    scanf("%lf%lf%lf", &C, &F, &X);
    R = 2.0;
    oldTime = X/2.0;
    newTime = 0.0;
    while(1) {
      newTime += C/R;
      R = R + F;
      newTime += X/R;
      if(newTime >= oldTime) break;
      oldTime = newTime;
      newTime -= X/R;
    }
   printf("Case #%d: %.7lf\n", iteration, oldTime);
  }
  return 0;
}


