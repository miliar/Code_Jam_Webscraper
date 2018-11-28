
#include <algorithm>
#include <cstdio>
#include <functional>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )
#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

double rd()
{
  double x;
  scanf("%lf", &x);
  return x;
}

const int N = 100;

double a[100][20];

int main()
{
  int cases = ri();
  REP1(_c, cases) {
    int n = ri();
    double v = rd(), t = rd();
    REP(i, n) {
      a[i][0] = rd();
      a[i][1] = rd();
    }

    printf("Case #%d: ", _c);
    if ( n==1) {
      if (a[0][1] == t)
        printf("%.7f\n", v/a[0][0]);
      else
        puts("IMPOSSIBLE");
    } else if (a[0][1] == a[1][1]) {
      if (a[0][1] == t)
        printf("%.7f\n", v/(a[0][0]+a[1][0]));
      else
        puts("IMPOSSIBLE");
    } else {
      double ma = max(a[0][1], a[1][1]), mi = min(a[0][1], a[1][1]);
      if (t < mi || t > ma)
        puts("IMPOSSIBLE");
      else {
        double q = (v * t - a[0][1] * v) / (a[1][1] - a[0][1]), p = v - q;
        printf("%.7f\n", max(p / a[0][0], q / a[1][0]));
      }
    }
  }
}
