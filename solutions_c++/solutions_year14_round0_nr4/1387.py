#include <cstdio>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

int main() {
   int t;
   scanf("%d", &t);

   for(int c = 1; c <= t; ++c) {
      int n;
      scanf("%d", &n);

      vector<double> naomi(n), ken(n);

      for(int i = 0; i < n; ++i)
         scanf("%lf", &naomi[i]);

      for(int i = 0; i < n; ++i)
         scanf("%lf", &ken[i]);

      int deceitfulPoints = 0,
          warPoints = 0;

      sort(naomi.begin(), naomi.end(), greater<double>());
      sort(ken.begin(), ken.end(), greater<double>());

      int pos = 0;
      for(int i = 0; i < n; ++i) {
         if(naomi[pos] > ken[i]) {
            ++deceitfulPoints;
            ++pos;
         }
      }

      pos = 0;
      for(int i = 0; i < n; ++i) {
         if(ken[pos] > naomi[i]) {
            ++warPoints;
            ++pos;
         }
      }

      warPoints = n - warPoints;

      printf("Case #%d: %d %d\n", c, deceitfulPoints, 
            warPoints);
   }
}
