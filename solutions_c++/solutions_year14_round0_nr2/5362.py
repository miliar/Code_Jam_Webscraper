#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

inline double go(double x, double rate) {
  return x / rate;
}

double go(double c, double f, double x) {
  double rate = 2;
  double res = go(x, rate);
  double t = 0;
  while (true) {
    t += go(c, rate);
    rate += f;
    double curr = t + go(x, rate);
    if (curr > res) return res;
    res = curr;
  }
}

int main() {
  int testCases; cin >> testCases;
  for (int caseNo = 1; caseNo <= testCases; caseNo++) {
    double c, f, x; cin >> c >> f >> x;
    printf("Case #%d: %.7f\n", caseNo, go(c, f, x));
  }
  return 0;
}
