#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;
  double C, F, X;
  for (int CASE = 1; CASE <= T; CASE++) {
    cin >> C >> F >> X;
    double p = 2;
    double t = 0;
    while (true) {
      if (X / p < C / p + X / (p + F)) {
        t += X / p;
        break;
      } else {
        t += C / p;
        p += F;
      }
    }
    printf("Case #%d: %.9f\n", CASE, t);
  }
}