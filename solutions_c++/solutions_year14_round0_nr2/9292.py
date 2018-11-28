

#include <iostream>
#include <iomanip>

using namespace std; 

int main(void) //Main Routine where the above written functions are called
{
	
   int numTestCases= 0;
   long double C,F,X;
   cin >> numTestCases;
   long double currRate, cookies;
   long double totalTime,timeToX,timeToC,cookieGain,timeToX2,cookies2;
   for (int tCount = 0; tCount < numTestCases; tCount++)
   {  
       totalTime= 0;
       cookies = 0;
   	   currRate = 2;	
       cin >>  C;
       cin >> F;
       cin >> X;

	   do {
	   	  timeToX = ((X-cookies)/currRate);
	   	  timeToC = ((C- cookies)/currRate);
	   	  cookies2 = cookies + (timeToC*currRate) - C;
	   	  timeToX2 = timeToC + ((X-cookies2)/(currRate+F));
	      if (timeToX < timeToX2 )
	   	  {
	   	    cookies += (X-cookies);
	   	    totalTime += timeToX;
	   	    break;
	      }
	      
	      totalTime += timeToC;
	      cookieGain = currRate*timeToC;
	      cookies += cookieGain;	      
	      currRate += F;
	      cookies -= C;
	   } while (cookies < X);
	 
	   cout << fixed << "Case #" << setprecision (7) << (tCount + 1) << ": " << totalTime << endl;
   }
   return 0 ;
}

