#include <iostream>
#include <cstdio>

using namespace std;

double eval(double C, double F, double X, int n)
{
  double time = 0;
  for (int j = 0; j < n + 1; ++j) {
    time += C / (2 + j * F);
  }
  time += X / (2 + F * (n + 1));

  return time;
}

int main(int argc, char **argv)
{
  int num_round;
  double C, F, X;

  cin >> num_round;
  for (int i = 0; i < num_round; ++i) {
    cin >> C >> F >> X;
    double time = 0;

    if (F * X < C * (F + 2)) {
      time = X / 2;
    } else {
      int n = (X * F / C - 2) / F - 1;
      time = std::min(eval(C, F, X, n), eval(C, F, X, n + 1));
    }
    printf("Case #%d: %.7f\n", i + 1, time);
  }

  return 0;
}
