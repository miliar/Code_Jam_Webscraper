#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

double c, f, x;

double solve(double a) {
  if (c/a + x/(a+f) < x/a) {
    return c/a + solve(a+f);
  }
  return x/a;
}

double solve2(double a) {
  double sum = 0;
  while (c/a + x/(a+f) < x/a) {
    sum += c/a;
    a += f;
  }
  sum += x/a;
  return sum;
}

int main() {
  //freopen("B-large.in", "r", stdin);
  //freopen("text.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
  int t, cases = 0;
  cin >> t;
  while (t--) {
    cin >> c >> f >> x;
    printf("Case #%d: %.7f\n", ++cases, solve2(2));
  }
  return 0;
} 
