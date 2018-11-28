#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <iomanip>

using namespace std;

struct Point {
  Point(double x_, double y_) : x(x_), y(y_) {}
  Point() : x(0), y(0) {}

  double x, y;
  Point shift(Point p) {
    return Point(x + p.x, y + p.y);
  }
  Point scale(double r) {
    return Point(x * r, y * r);
  }
};

const double EPS = 1e-12;
const int N_MAX = 128;
int N;
double V, X;
double rates[N_MAX];
double temps[N_MAX];
Point contour[2 * N_MAX];

bool compare_slope(Point a, Point b) {
  return a.y * b.x < b.y * a.x;
}

void init() {
  cin >> N >> V >> X;

  for (int i = 0; i < N; i++) {
    cin >> rates[i] >> temps[i];
    contour[i] = Point(rates[i], rates[i] * temps[i]);
  }

  sort(contour, contour + N, compare_slope);
  for (int i = 0; i < N; i++) {
    contour[N + i] = contour[i].scale(-1);
  }
}

// returns true if it is an extreme case
// answer is -1 if impossible
bool handle_extreme_cases(double *answer) {
  double min_temp = 100, max_temp = 0;

  for (int i = 0; i < N; i++) {
    min_temp = min(min_temp, temps[i]);
    max_temp = max(max_temp, temps[i]);
  }

  if (min_temp > X || max_temp < X) {
    *answer = -1;
    return true;
  }

  if (min_temp == X || max_temp == X) {
    double rate = 0.0;
    for (int i = 0; i < N; i++) {
      if (temps[i] == X)
        rate += rates[i];
    }
    *answer = V / rate;
    return true;
  }

  return false;
}

void solve_case(int t) {
  init();
  double answer = 0.0;
  if (handle_extreme_cases(&answer)) {
    cout << "Case #" << t << ": ";
    if (answer == -1)
      cout << "IMPOSSIBLE\n";
    else
      cout << fixed << setprecision(10) << answer << "\n";
    return;
  }

  Point cur = contour[0];
  for (int i = 1; i < 2 * N; i++) {
    assert(i != 2 * N - 1);
    Point next = cur.shift(contour[i]);
    if (next.y < X * next.x) {
      // temp still too low
      cur = next;
      continue;
    }

    double r_min = 0, r_max = 1;
    while (r_max - r_min > EPS) {
      double mid = (r_min + r_max) / 2;
      next = cur.shift(contour[i].scale(mid));
      if (next.y < X * next.x) {
        r_min = mid;
      } else {
        r_max = mid;
      }
    }

    /*
    cout << "i is " << i << endl;
    cout << "r is " << r_min << " to " << r_max << endl;
    */

    cur = cur.shift(contour[i].scale(r_min));
    break;
  }

  /*
  if (abs(cur.y / cur.x - X) > 1000 * EPS) {
    cout << "what " << cur.x << ", " << cur.y << endl;
    cout << cur.y / cur.x << endl;
    cout << X << endl;
    assert(false);
  }
  */

  answer = V / cur.x;
  cout << "Case #" << t << ": "
       << fixed << setprecision(10) << answer << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
