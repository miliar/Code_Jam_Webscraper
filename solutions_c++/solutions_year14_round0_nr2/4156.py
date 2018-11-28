#include <iostream>
#include <stdio.h>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    double C, F, X;
    cin >> C;
    cin >> F;
    cin >> X;
    double t = (X / C) - (2 / F) - 1;
    double total_time = 0;
    double final_rate = 2;
    for (int j = 0 ; j < t; ++j) {
      total_time += (C / (2 + j*F));
      final_rate += F;
    }
    total_time += X/final_rate;
    printf("Case #%d: %0.7f\n", i, total_time);
  }
  return 0;
}
