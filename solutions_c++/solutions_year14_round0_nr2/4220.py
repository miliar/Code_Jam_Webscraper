#include <iostream>
#include <vector>

using namespace std;

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int Case = 1; Case <= nCases; ++Case) {
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double T = 0;
    int i = 0;
    double ans = X / 2;
    while (T < ans) {
      ++i;
      T = T + C /(2 + (i - 1) * F);
      ans = min(ans, T + X / (2 + i * F));
    }
    printf("Case #%d: %.7lf\n", Case, ans);
  }
  return 0;
}
