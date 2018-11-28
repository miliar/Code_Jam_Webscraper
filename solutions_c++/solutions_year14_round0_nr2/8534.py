#include <cassert>
#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

typedef pair<double, double> line;

const double eps = 1e-7;
double t;
line current_line;
double C, F, X;

int cmp(double x, double y)
{
  if (x + eps < y) return -1;
  if (y + eps < x) return +1;
  return 0;
}

double eval(const line & r, double x)
{
  return r.first * x + r.second;
}

double time_to_y(const line & r, double y)
{
  return (y - r.second) / r.first;
}

double intersection(const line & r, const line & s)
{
  assert(!cmp(r.first, s.first));
  return (s.second - r.second) / (r.first - s.first);
}

int main()
{
  int ntc; cin >> ntc;
  for (int tc = 1; tc <= ntc; ++tc) {
    scanf("%lf%lf%lf", &C, &F, &X);
    current_line = line(2.0, 0.0);
    printf("Case #%d: ", tc);
    while (true) {
      double t_X = time_to_y(current_line, X);
      double t_buy = time_to_y(current_line, C);
      line candidate_line(current_line.first + F, - (current_line.first + F) * t_buy);
      double t_X_buy = time_to_y(candidate_line, X);
      if (t_X < t_X_buy) {
        printf("%.7lf\n", t_X);
        break;
      } else {
        current_line = candidate_line;
      }
    }
  }
}
