#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;

double compute(int N, double V, double X, vector<double>& R, vector<double>& C) {
  if (N == 1) {
    if (C[0] != X) return -1;
    return V / R[0];
  }

  if (N == 2) {
    if (C[0] > X && C[1] > X) return -1;
    if (C[0] < X && C[1] < X) return -1;

    if (C[0] == C[1]) return V / (R[0] + R[1]);
    if (C[0] == X) return V / R[0];
    if (C[1] == X) return V / R[1];

    double hore = V*X - V*C[1];
    double dole = C[0] - C[1];

    double V1 = hore / dole;
    double V2 = V - V1;

    double T1 = V1 / R[0];
    double T2 = V2 / R[1];

    if (fabs(V1+V2 - V) > 1e-10) fprintf(stderr, "huh!\n");
    if (fabs((V1*C[0]+V2*C[1])/V - X) > 1e-10) fprintf(stderr, "huh!\n");
    if (min(T1, T2) < 0) fprintf(stderr, "min %lf %lf\n", T1, T2);

    if (T1 < -1e-10 || T2 < -1e-10) return -1;

    return max(T1, T2);
  }

  fprintf(stderr, "big\n");
  return -1;  // XXX
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int N;
    double V, X;
    scanf("%d %lf %lf", &N, &V, &X);

    vector<double> R(N), C(N);
    for (int i = 0; i < N; i++) scanf("%lf %lf", &R[i], &C[i]);

    double res = compute(N, V, X, R, C);

    fprintf(stderr, "case %d: %d (%lf,%lf) ", tc, N, V, X);
    for (int i = 0; i < N; i++) fprintf(stderr, "(%lf,%lf) ", R[i], C[i]);
    if (res == -1) fprintf(stderr, "IMPOSSIBLE\n");
    else fprintf(stderr, "%.12lf\n", res);

    printf("Case #%d: ", tc);
    if (res == -1) printf("IMPOSSIBLE\n");
    else printf("%.12lf\n", res);
  }
}
