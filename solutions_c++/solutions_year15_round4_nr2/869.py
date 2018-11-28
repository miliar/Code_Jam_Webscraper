// C++11
#include <cstdio>
#include <algorithm>
#include <gmpxx.h>
using namespace std;

const double EPS = 1e-13;

int main() {
  int T; scanf("%d", &T);
  for(int tci = 0; tci < T; ++tci) {
    int N; double V_d, Xarg_d; scanf("%d%lf%lf", &N, &V_d, &Xarg_d);
    mpz_class V = V_d * 10000 + 0.5;
    mpz_class Xarg = Xarg_d * 10000 + 0.5;
    mpz_class VX = V * (1000000 - Xarg);
    mpz_class VY = V * Xarg;
    static mpz_class R[100], C[100], X[100], Y[100];
    for(int i = 0; i < N; ++i) {
      double Rd, Cd;
      scanf("%lf%lf", &Rd, &Cd);
      R[i] = Rd * 10000 + 0.5;
      C[i] = Cd * 10000 + 0.5;
      X[i] = R[i] * (1000000 - C[i]);
      Y[i] = R[i] * C[i];
    }
    mpz_class Xsum = 0, Ysum = 0;
    for(int i = 0; i < N; ++i) {
      Xsum += X[i];
      Ysum += Y[i];
    }
    mpq_class minval = -1;
    for(int i = 0; i < N; ++i) {
      mpz_class Xi = X[i];
      mpz_class Yi = Y[i];
      mpz_class Xsum_i = Xsum - X[i];
      mpz_class Ysum_i = Ysum - Y[i];
      mpz_class det = Xsum_i * Yi - Xi * Ysum_i;
      mpq_class x1, x2;
      if(det == 0) {
        if(VX * Ysum == VY * Xsum) {
          x1 = x2 = (mpq_class)(VX + VY) / (Xsum + Ysum);
        } else continue;
      } else {
        mpz_class xx1 = Yi * VX - VY * Xi;
        mpz_class xx2 = Xsum_i * VY - VX * Ysum_i;
        if(xx1 < 0 || xx2 < 0) continue;
        x1 = (mpq_class)xx1 / det;
        x2 = (mpq_class)xx2 / det;
      }
      if(x1 >= 0 && x2 >= 0) {
        mpq_class x1x2max = max(x1, x2);
        if(minval == -1 || minval > x1x2max) {
          minval = x1x2max;
        }
      }
    }
    if(minval == -1) {
      printf("Case #%d: IMPOSSIBLE\n", tci+1);
    } else {
      printf("Case #%d: %.20f\n", tci+1, minval.get_d());
    }
  }
  return 0;
}
