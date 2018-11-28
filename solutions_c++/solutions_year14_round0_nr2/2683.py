#include <cstdio>
#include <cstdlib>

using namespace std;
int T;
double C, F, X;
double direct(double remain, double speed) {
  return remain / speed;
}
double notdirect(double remain, double speed) {
  double a = C / speed;
  double b = remain / (speed + F);
  return a+b;
}
int main() {
  scanf("%d", &T);
  for(int c=1; c<=T; c++) {
    double ret = 0, speed = 2, sa, sb;
    scanf("%lf%lf%lf", &C, &F, &X);
    while(true) {
      sa = direct(X, speed);
      sb = notdirect(X, speed);
      if(sa < sb) {
        ret += sa;
        break;
      }
      ret += C / speed;
      speed += F;
    }
    printf("Case #%d: %.7lf\n", c, ret);
  }
  return 0;
}
