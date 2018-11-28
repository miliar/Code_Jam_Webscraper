#include <cstdio>

using namespace std;

int main() {
   int t;
   scanf("%d", &t);

   for(int c = 1; c <= t; ++c) {
      double rate = 2,
             farmCost, farmRate, target;

      scanf("%lf %lf %lf", &farmCost, &farmRate, &target);

      double addedTime = 0, 
             time, buyingOther;
      do {
         // Ending now...
         time = addedTime + target / rate;

         // Buying other farm...
         addedTime += farmCost / rate;
         rate += farmRate;
         buyingOther = addedTime + target / rate;
      } while(buyingOther < time);

      printf("Case #%d: %.7lf\n", c, time);
   }
}
