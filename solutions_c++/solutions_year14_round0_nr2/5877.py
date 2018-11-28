#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream fin("b.in");
  int T;
  fin >> T;

  double C, F, X;

  ofstream fout("b.out");
  for (int t = 1; t <= T; ++t) {
    fin >> C >> F >> X;

    double tmp = X / C - 2.0 / F;
    int n = tmp > 0 ? floor(tmp) : 0;

    double tm = 0.0;
    for (int i = 0; i < n; ++i)
      tm += C / (2.0 + i * F);
    tm += X / (2.0 + n * F);

    fout.precision(7);
    fout << "Case #" << t << ": " << fixed << tm << endl;
  }
  return 0;
}
