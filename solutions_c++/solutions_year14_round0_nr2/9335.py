
#include <cstdio>
#include <set>
using namespace std;

int main() {
  int T;
  scanf(" %d", &T);
  for (int test = 1; test <= T; ++test) {
    double C, F, X;
    scanf(" %lf %lf %lf", &C, &F, &X);

    double bt = X / 2.0;
    for (int f = 0; ; ++f) {

      double t = 0.0;
      double cur = 2.0;
      for (int i = 0; i < f; ++i) {
        t += C / cur;
        cur += F;
      }

      if (t > bt) {
        break;
      }

      t += X / cur;

      if (t < bt) {
        bt = t;
      }
    }

    printf("Case #%d: %.7lf\n", test, bt);
  }

  return 0;
}
