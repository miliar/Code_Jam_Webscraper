#include <iostream>
#include <cstdio>

using namespace std;

double find_fastest(int N, double C, double F, double X) {

  double fastest = 0.0;
  for (int n = 0; n < N; n++) {
    fastest += C/(2.0 + n*F);
  }
  fastest += X/(2.0 + N*F);
  return fastest;
}

int main() {
  int T;

  cin >> T;
  for (int t = 1; t <= T; t++) {

    double C, F, X;
    cin >> C >> F >> X;

    double cookie_rate = 2.0;

    double fastest = X*0.5;
    double old_fastest = X;
    int N = 1;
    double Csum = 0.0;

    while (old_fastest > fastest) {
      old_fastest = fastest;
      Csum += C/(2.0 + (N-1)*F);
      fastest = Csum + X/(2.0 + N*F);
      N++;
    }

    cout << "Case #" << t << ": ";

    printf("%.7f", old_fastest);

    cout << endl;
  }

  return 0;
}
