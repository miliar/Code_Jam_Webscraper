/* Written by Filip Hlasek 2014 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  REP(tt, T) {
    printf("Case #%d: ", tt + 1);
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double income = 2;
    double t = 0, best = X / income, total = X / income;
    bool better;
    do {
      better = false;
      double delta_time = C / income;
      t += delta_time;
      income += F;
      double total = t + X / income;
      if (total < best) {
        better = true;
        best = total;
      }
    } while(better);
    printf("%.10lf\n", best);
  }
  return 0;
}
