#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)

#ifdef WIN32  
#define LLD "%I64d"
#else 
#define LLD "%Ld"
#endif

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const double inf = (double) 1e9;
const int maxn = (int) 1e5 + 1;
const double eps = (double) 1e-8;

int main() {
  
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    double c, f, x, d[maxn]; int p = 0;
    d[0] = 0.0;
    scanf("%lf%lf%lf", &c, &f, &x);
    double ans = x / 2.0;
    while (ans > d[p]) {
      p++;
      d[p] = d[p - 1] + c / ((p - 1) * f + 2.0);
      double s = d[p] + x / (p * f + 2.0);
      ans = min(ans, s);
    }
    printf("Case #%d: %.10lf\n", test, ans);
  }

  return 0;
}
