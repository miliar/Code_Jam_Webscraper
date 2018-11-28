#define B
#ifdef B

#include <iostream>

using namespace std;

int main() {
	int T, t = 0;
   cin >> T;

	while ( t++ < T ) {
      double farmCost, farmPerSec, cookiesToWin;
      cin >> farmCost >> farmPerSec >> cookiesToWin;
      double cookies = 0, secondsElapsed = 0, cookieRate = 2.0;

      while ( cookies < cookiesToWin )
      {
         double timeToWinAtCurrentPace = (cookiesToWin - cookies) / cookieRate;
         double timeToBuyAFarmAtCurrentPace = (farmCost - cookies) / cookieRate;
         double timeToWinWithAnotherFarm = timeToBuyAFarmAtCurrentPace + (cookiesToWin / (cookieRate + farmPerSec) );

         if ( timeToWinAtCurrentPace <= timeToWinWithAnotherFarm )
         {
            cookies += timeToWinAtCurrentPace * cookieRate;
            secondsElapsed += timeToWinAtCurrentPace;
         }
         else
         {
            secondsElapsed += timeToBuyAFarmAtCurrentPace;
            cookies = 0;
            cookieRate += farmPerSec;
         }
      }

      printf("Case #%d: %.7f\n", t, secondsElapsed);
	}
	return 0;
}
#endif