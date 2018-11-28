#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

double farm[100001];
int main() {

  int TC;

  cin >> TC;

  for (int tc = 1; tc <= TC; tc++) {
    double C, F, X;
    
    cin >> C >> F >> X;
    memset(farm, 0, sizeof(double)*100001);

    double now = 2;

    for (int i = 1; i <= 100001; i++) {
      farm[i] = farm[i-1] + (C / now);
      now += F;
    }

    for (int i = 0; i <= 100001; i++) {
      farm[i] += (X / (F * i + 2));
    }

    double min = farm[0];
    for (int i = 1; i <= 100001; i++) {
      if (min > farm[i]) min = farm[i];
    }

    printf("Case #%d: %.7lf\n", tc, min);

  }
  return 0;
}
