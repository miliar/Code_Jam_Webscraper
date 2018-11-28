#include <algorithm>
#include <assert.h>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <numeric>
#include <limits>
#include <iomanip>
using namespace std;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define LL long long
#define LD long double
#define vi vector<int>
#define vl vector<LL>
#define vs vector<string>
#define vb vector<bool>
#define ii pair<int, int>
#define vii vector<ii>
#define SET(v, i) (v | (1 << i))
#define TEST(v, i) (v & (1 << i))
#define TOGGLE(v, i) (v ^ (1 << i))

ofstream debug("debug.txt");

double SolveImpl(double c, double f, double x, double r, double penalty) {
  if (penalty > x / 2.0)
    return x / 2.0;

  double time_to_finish = penalty + x / r;

  debug << penalty << "\t" << time_to_finish << endl;
  return min(time_to_finish, SolveImpl(c, f, x, r + f, penalty + c / r));
}

double SolveIter(double c, double f, double x) {
  double r = 2;
  double prev = 1000 * 1000 * 2, sol = 1000 * 1000;
  double penalty = 0;
  while (abs(sol - prev) > 1e-7) {
    prev = sol;
    double curr = penalty + x / r;
    sol = min(sol, curr);
    penalty += c / r;
    if (penalty > x / 2 || prev < curr)
      break;

    r += f;
  }

  return sol;
}

double Solve(double c, double f, double x) {
  //debug << "**************************" << c << "\t" << f << "\t" << x << endl;
  //return SolveImpl(c, f, x, 2, 0);
  return SolveIter(c, f, x);
}

int main() {
  ifstream cin("B-small-attempt2.in");
  ofstream cout("submit.txt");

  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    double c,f,x;
    cin >> c >> f >> x;
    cout << "Case #" << tt << ": ";
    cout << std::fixed << std::setprecision(7) << Solve(c, f, x) << endl;
  }
  return 0;
}
