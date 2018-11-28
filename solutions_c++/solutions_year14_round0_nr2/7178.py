#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main()
{
   int T;
   
   cin >> T;
   for(int idx = 1; idx <= T; ++idx)
   {
		double C, F, X;
		
		cin >> C >> F >> X;
		
		double rate = 2.0;
		double toBuyFarm = C / rate, toObtainX = X / rate, totalTime = 0.0;
		
		while(true)
		{
			if(toObtainX <= toBuyFarm)
			{
				totalTime += toObtainX;
				break;
			}
			else {
					double falseTime = toBuyFarm + (X / (rate + F)) + totalTime;
					
					if(falseTime < totalTime + toObtainX)
					{
						totalTime += toBuyFarm;
						rate += F;
						toBuyFarm = C / rate;
						toObtainX = X / rate;
					}
					else {
							 totalTime += toObtainX;
							 break;
						 }
				 }
		}
		
		cout << fixed << setprecision(7) << "Case #" << idx << ": " << totalTime << '\n';
   }

   return EXIT_SUCCESS;
}