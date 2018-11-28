#include<iostream>
#include<cstdio>

using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); ++i)

void solve() {
  double c, f, x;
  cin >> c >> f >> x;
  double res = 1e9;
  double time = 0;
  double cps = 2;
  while (time < res) {
    res = min(res, time + x / cps);
    time += c / cps;
    cps += f;
  }
  printf("%.7lf\n", res);
}

int main() {
  int t;
  cin >> t;
  rep (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
