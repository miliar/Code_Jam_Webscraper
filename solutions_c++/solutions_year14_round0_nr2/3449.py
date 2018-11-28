#include <cstdio>
#include <vector>

using namespace std;

void Solve() {
   double C, F, X;
   scanf("%lf %lf %lf", &C, &F, &X);
   int nrFarms = 0;
   double now = 0.0;
   double best = 1e20;

   while (now < best) {
      double ratePerSec = 2.0 + nrFarms * F;
      double nextFarm = now + C / ratePerSec;
      double finishTime = now + X / ratePerSec;
      if (finishTime < best) {
         best = finishTime;
      }
      //else {
      //   break;
      //}
      now = nextFarm;
      nrFarms++;
   }

   printf("%.8lf\n", best);
}

int main() {
   freopen("data.in", "rb", stdin);
   freopen("data.out", "wb", stdout);
   int tst;
   scanf("%d", &tst);
   for (int i = 1; i <= tst; i++) {
      printf("Case #%d: ", i);
      Solve();
   }
}