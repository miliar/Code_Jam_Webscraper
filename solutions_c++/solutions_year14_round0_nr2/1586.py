#include <iostream>
#include <vector>
#include <set>

const double eps = 1e-8;

double solve(long double c, long double f, long double x) {
  const long double alpha = x / c;
  const long double nd = alpha - 2 / f;
  const int n = nd + eps;
  //std::cerr << "solve(" << c << ", " << f << ", " << x << "):" << n << '\n';
  if(nd <= eps) return x / 2;

  long double sol = 0;
  for(int i=0;i<n;i++)
    sol += 1.0 / (f * i + 2);
  sol = sol * c + x / (n * f + 2);
  return sol;
}

int main() {
  int T;
  using std::cin;
  using std::cout;
  using std::cerr;
  cin >> T;
  cout.precision(7);
  cout << std::fixed;
  for(int tcase=1;tcase<=T;++tcase) {
    double c, f, x;
    cin >> c >> f >> x;
    cout << "Case #" << tcase << ": " << solve(c, f, x) << '\n';
  }
}
