#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

double solve2(double factoryCost, double factoryGain, double limit, double perSecond) { 
   double missing = limit;
   double timeSpent = 0;
   double cookiesPerSec = perSecond;
   double timeToNextFactory = factoryCost / cookiesPerSec;
   double timeToFinishWithNextFactory = timeToNextFactory + (missing + factoryCost - (timeToNextFactory * cookiesPerSec)) / (cookiesPerSec + factoryGain); 
   double timeToFinishWithoutNextFactory = missing / cookiesPerSec;
   while (timeToFinishWithNextFactory < timeToFinishWithoutNextFactory) {
      timeSpent += timeToNextFactory;
      limit -= timeToNextFactory*cookiesPerSec;
      cookiesPerSec += factoryGain; 
      timeToNextFactory = factoryCost / cookiesPerSec;
      timeToFinishWithNextFactory = timeToNextFactory + (missing + factoryCost - (timeToNextFactory * cookiesPerSec)) / (cookiesPerSec + factoryGain);
      timeToFinishWithoutNextFactory = missing / cookiesPerSec;
   }
   return timeSpent + timeToFinishWithoutNextFactory;   
}

double solve(double factoryCost, double factoryGain, double limit, double perSecond, double produced) {
   double missing = limit - produced;
   if (missing < perSecond) {
      return missing/perSecond;
   }
   double timeToNextFactory = produced >= factoryCost ? 0 : (factoryCost - produced) / perSecond;
   double productionGainTillFactoryBought = timeToNextFactory * perSecond; 
   double newProduced = produced - factoryCost + productionGainTillFactoryBought;
   double newperSecond = perSecond + factoryGain;
   double timeIfFactoryBought = timeToNextFactory + solve(factoryCost, factoryGain, limit, newperSecond, newProduced); 
   double timeIfFactoryNotBought = missing / perSecond;
   return timeIfFactoryBought < timeIfFactoryNotBought ? timeIfFactoryBought : timeIfFactoryNotBought; 
}

double solve(double c, double f, double x) { 
   return solve2(c, f, x, 2);
}

int main(int argc, char ** argv) {
   int cases;

   cin >> cases; 
   for (int i = 0; i < cases; i++) {
      double c,f,x;
      cin >> c;
      cin >> f;
      cin >> x;
      //cout << "Case #" << i+1 << ": " << setprecision(7) << solve(c,f,x) << endl; 
      printf("Case #%d: %.7f\n", i+1, solve(c,f,x));
   }

   return 0;
}
