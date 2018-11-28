#include <iostream>
using namespace std;

double calc(int buy, double C, double F, double X) {
  double res = 0;
  for (int i = 0; i < buy; i++) {
    res += C / (2.0 + F * i);
  }
  res += X / (2.0 + F * buy);
  return res;
}

double test(double C, double F, double X) {
  double last_result = X / 2.0, now;
  int buy = 1;
  while ( (now = calc(buy++, C, F, X)) < last_result) {
    last_result = now;
  }
  return last_result;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    double C, F, X;
    cin >> C >> F >> X;
    printf("Case #%d: %.7f\n", i+1, test(C, F, X));
  }
}
  
