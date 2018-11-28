#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
using namespace std;

int main() {
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int t, caset;
  cin >> t;
  caset = 0;
  cout.setf(ios::fixed);
  while(caset < t) {
    caset ++;
    cout << "Case #" << caset << ": ";
    double c, f, x;
    cin >> c >> f >> x;
    double ans = -1.0;
    for (int i = 0; i <= 10000; ++i){
      double now = 0.0;
      double nowrate = 2.0;
      for (int j = 0; j < i; ++j) {
        now = now + c / nowrate;
        nowrate = nowrate + f;
        if (ans > 0 && now > ans) break;
      }
      now = now + x / nowrate;
      if (ans < 0 || now < ans) ans = now;
    }
    cout << setprecision(10) << ans << endl;
  }
  return 0;
}
