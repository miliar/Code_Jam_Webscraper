#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;

struct Source {
  double v, x;
  bool operator <(const Source& b) const {
    return x < b.x;
  }
};

int N;
double V, X;
Source s[100];

double Solve() {
  if (N == 1) {
  if (X != s[0].x) return -1;
    return V / s[0].v;
  }
  if (X < s[0].x || s[1].x < X) return -1;
  if (X == s[0].x && X == s[1].x) {
    return V / (s[0].v + s[1].v);
  }
  double dx0 = X - s[0].x;
  double dx1 = s[1].x - X;
  double t0 = (V * dx1 / (dx0 + dx1)) / s[0].v;
  double t1 = (V * dx0 / (dx0 + dx1)) / s[1].v;
  return max(t0, t1);
}

int main() {
  int nnn;
  cin >> nnn;
  for (int iii = 0; iii < nnn; ++iii) {
    cin >> N >> V >> X;
    for (int i = 0; i < N; ++i) {
      cin >> s[i].v >> s[i].x;
    }
    sort(s, s+N);
    double ans = Solve();
    if (ans < 0)
      cout << "Case #" << iii+1 << ": IMPOSSIBLE" << endl;
    else {
      char r[1024];
      sprintf(r, "%.8f", ans);
      cout << "Case #" << iii+1 << ": " << r << endl;
    }
  }
}
