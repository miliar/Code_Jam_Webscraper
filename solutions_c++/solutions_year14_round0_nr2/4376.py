#include<iostream>
#include<cmath>

using namespace std;

int main() {
  int T;
  double C, F, X, t;
  int n;
  cin >> T;
  for (int ti = 0; ti < T; ti++) {
    cin >> C >> F >> X;
    n = (int) ceil(((X - C) * (F + 2) - 2 * X) / (C * F));
    n = (n > 0 ? n : 0);
    t = 0;
    for (int i = 0; i < n; i++) {
      t += C / (i * F + 2);
    }
    t += X / (n * F + 2);
    printf("Case #%d: %.7lf\n", ti + 1, t);
  }
  return 0;
}
