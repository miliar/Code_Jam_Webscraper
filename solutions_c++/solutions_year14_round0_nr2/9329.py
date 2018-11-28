#include <iostream>
#include <cstdio>

using namespace std;

double timeRequired(double c, double f, double x, int n) {
  double accum = 0.0;

  for (int i = 0; i < n; i++) {
    accum += (c / (2 + i*f));
  }

  accum += (x / (2 + n*f));
  return accum;
}

int main(int argc, char* argv[]) {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    double c, f, x;
    cin >> c >> f >> x;

    int n = 0;
    double min = timeRequired(c, f, x, n);
    while (true) {
      n++;
      double next = timeRequired(c, f, x, n);
      if (next < min)
        min = next;
      else
        break;
    }

    printf("Case #%d: %.8f\n", i+1, min);
  }
}
