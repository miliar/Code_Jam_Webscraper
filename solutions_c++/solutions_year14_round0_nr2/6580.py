// Warm up question.

#include <iostream>
#include <vector>

using namespace std;

int main() {
  int TC;
  double C, F, X;
  scanf("%d ", &TC);
  for (int tc = 1; tc <= TC; ++tc) {
    scanf("%lf %lf %lf ", &C, &F, &X);
    double rate = 2.0;
    double prev = X / rate;
    double sum = 0.0;
    while (true) {
      sum += C / rate;
      rate += F;
      double newValue = sum + (X / rate);
      if (newValue >= prev) {
        break;
      } else {
        prev = newValue;
      }
    }
    printf("Case #%d: %.7lf\n", tc, prev);
  }
  return 0;
}
