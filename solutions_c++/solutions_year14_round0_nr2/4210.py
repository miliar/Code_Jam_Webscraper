#include <cstdio>

double endtime(double x, double c, double f, double rate) {
  double best = 1e100;
  double t = 0.0;
  for(;;) {
    if (t + (x / rate) > best) {
      return best;
    }
    best = t + (x / rate);
    t += c / rate;
    rate += f;
  }
}
int main() {
  int nump;
  scanf("%d", &nump);
  for (int i = 0; i < nump; ++i) {
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    printf("Case #%d: %.8lf\n", i+1, endtime(x, c, f, 2.0));
  }
}
