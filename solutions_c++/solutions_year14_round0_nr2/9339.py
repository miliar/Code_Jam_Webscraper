#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
using namespace std;  
const double EPS = 0.00000001;
int main() {
  int tt;
  cin >> tt;
  for(int test = 1; test <= tt; ++test) {
    double c, f, x, cookies = 2;
    cin >> c >> f >> x;
    double t = 0;
    double sum = 0;
    while(fabs(x - sum) > EPS) {
      if((x / cookies) > (c / cookies) + (x / (cookies + f))) {
        t += c / cookies;
        cookies += f;
      } else {
        t += x / cookies;
        sum  = x;
      }
    }

    cout << "Case #" << test << ": " << fixed << setprecision(7) << t << '\n';
  }

  return 0;
}
