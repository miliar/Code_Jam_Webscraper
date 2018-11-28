#include <iostream>

using namespace std;

void solve(int TEST) {
  long double C, F, X;

  cin >> C >> F >> X;

  long double m = 2.0;
  long double b = 0;

  while (true) {
    //printf("At %Lf: speed %Lf\n", b, m);

    long double x1 = X / m + b;
    long double x2 = C / m + b;
    long double x3 = X / (m + F) + x2;

    //printf("%Lf vs %Lf (%Lf)\n", x1, x3, x2);

    if (x1 < x3) {
      printf("Case #%d: %.7Lf\n", TEST, x1);
      break;
    } else {
      b = x2;
      m += F;
    }
  }

}

int main() {
  int n = 0;

  cin >> n;
  for (int i = 0; i < n; i++) {
    solve(i+1);
  }
}

