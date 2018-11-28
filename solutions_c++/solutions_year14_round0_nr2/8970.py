#include <iostream>
#include <iomanip>

using namespace std;

long double ProjectTime( long double cookies, unsigned int farms, long double f, long double x )
{
   long double goal = x - cookies;
   long double timeRemaining = goal / (farms * f + 2);
   return timeRemaining;
}

int main()
{
   unsigned int testCases;
   cin >> testCases;
   for( size_t l = 1; l <= testCases; ++l )
   {
      long double c, f, x; //c cost, f cookies/s, x goal
      long double cookies = 0;
      long double time = 0.0;
      unsigned int farms = 0;
      long double timePassed;
      cin >> c >> f >> x;

      while( cookies < x )
      {
	 timePassed = min( c / (farms * f + 2), (x - cookies) / (farms * f + 2) );

	 time += timePassed;
	 cookies += timePassed * 2;
	 cookies += (timePassed * farms * f);
	 if( cookies >= x )
	 {
	    break;
	 }
	 if( ProjectTime( cookies, farms, f, x ) > ProjectTime( cookies - c, farms + 1, f, x ) )
	 {
	    //buy farm
	    ++farms;
	    cookies -= c;
	 }
	 else
	 {
	    //calculate remaining time
	    time = time + ProjectTime( cookies, farms, f, x );
	    break;
	 }
	 
      }
      cout << std::fixed << std::setprecision(7);
      cout << "Case #" << l << ": " << time << endl;
   }

   return 0;
}
