#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <set>
#include <sstream>
using namespace std;

fstream in, out;

int T;
double C, F, X;
string ans;
double cookie_rate;

double compute(int N) {
  if (N < 0) {
    return compute(0);
  }
  double ret = 0;
  for (int i = 0; i < N; ++i) {
    ret += 1.0 / (2.0 + i * F);
  }
  ret *= C;
  ret += X / (2.0 + N * F);
  return ret;
}

int main() {
  in.open("B-large.in", fstream::in);
  out.open("probb-large.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; i++) {
    in >> C;
    in >> F;
    in >> X;
    cout << std::fixed << std::setprecision(7) << "Case " << i << ": " << C << " " << F << " " << X << endl;

    double N = (X * F - 2 * C) / (C * F);
    cout << N << endl;
    stringstream ss;
    ss << std::fixed << std::setprecision(7) << compute((int)N);
    ans = ss.str();
    out << "Case #" << i + 1 << ": " << ans << endl;
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
