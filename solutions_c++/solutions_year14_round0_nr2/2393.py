#include <cstdio>
#include <iostream>
using namespace std;

double solve(double c, double f, double x, double rate)
{
  if (x <= c) {
    return x / rate;
  } else if (c/rate+x/(f+rate) < x/rate) {
    return c / rate + solve(c, f, x, f+rate);
  } else {
    return x / rate;
  }
}

int main()
{
  int n;
  double c, f, x;
  cin >> n;

  for (int i = 1; i <= n; ++i) {
    cin >> c >> f >> x;
    printf("Case #%d: %.8f\n", i, solve(c, f, x, 2.0));
  }
  
  return 0;
}
