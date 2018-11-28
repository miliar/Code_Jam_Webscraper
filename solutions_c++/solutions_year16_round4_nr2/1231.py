#include <cstdio>

#include <vector>
#include <cstring>

using namespace std;

#define BITCOUNT(mask) ( __builtin_popcount((mask)) )

int N, K;
double P[16];

bool cached[16][16];
double memo[16][16];
double go(vector<double>& pr, int k, int nyes) {
   if (nyes < 0) return 0.0;
   if (k == 0)
      return nyes == 0 ? 1.0 : 0.0;
   if (!cached[k][nyes]) {
      double& res = memo[k][nyes];
      // k-1 th member votes yes
      res = pr[k-1] * go(pr, k-1, nyes-1) +
            (1 - pr[k-1]) * go(pr, k-1, nyes);
      cached[k][nyes] = true;
   }
   return memo[k][nyes];
}

double sim(vector<double>& pr) {
   memset(cached, 0, sizeof(cached));
   return go(pr, K, K/2);
}

double solve() {
   double res = 0.0;
   for (int mask = (1<<N)-1; mask > 0; --mask) {
      if (BITCOUNT(mask) != K) continue;
      vector<double> pr;
      for (int i = 0; i < N; ++i) {
         if (mask & (1<<i))
            pr.push_back(P[i]);
      }
      double cur = sim(pr);
      res = max(res, cur);
   }
   return res;
}

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d %d", &N, &K);
      for (int i = 0; i < N; ++i)
         scanf("%lf", P+i);
      double res = solve();
      printf("Case #%d: %.08f\n", tc, res);
   }

   return 0;
}
