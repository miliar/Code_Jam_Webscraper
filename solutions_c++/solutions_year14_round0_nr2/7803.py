#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[])
{
  double C, F, X;
  int tn;
  cin >> tn;
  for (int ti = 1; ti <= tn; ++ti) {
    cin >> C >> F >> X;
    double rate = 2.0 + F;
    double sum = 0.5;
    double prev;
    double minvalue = X / 2.0;
    for (int i = 0; ; ++i) {
      prev = sum;
      sum += 1 / rate;
      minvalue = min(minvalue, C*prev + X/rate);
      rate += F;
      if (X/rate < 0.01) break;
    }
    printf("Case #%d: %.7lf\n", ti, minvalue);
  }
  return 0;
}
