#include <cstdio>
#include <iostream>
#include <cassert>
#include <ctime>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>

using namespace std;

typedef long long int int64;
typedef long double ext;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#ifdef LOCALD
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) {}
#endif

int T;

const int MAX_FARMS = 5000;
const double inf = 1e+9;
const double sp = 2.0;
double c, f, x;


int main() {
  assert(scanf("%d", &T) == 1);
  for (int test = 1; test <= T; test++) {
    assert(scanf("%lf %lf %lf", &c, &f, &x) == 3);
    double ans = inf;
    double s = sp;
    double t = 0.0;
    for (int farms = 0; farms <= MAX_FARMS; farms++) {
      ans = min(ans, t + x / s);
      t += c / s;
      s += f;      
    }
    printf("Case #%d: %.8lf\n", test, ans);
  }
  return 0;
}