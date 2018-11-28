#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int main()
{
	int tc;
	cin >> tc;
	for(int cn = 1; cn <= tc; cn++)
	{
		long double time = 0;
		long double c;
		long double f;
		long double x;
		cin >> c;
		cin >> f;
		cin >> x;

		long double rate = 2;
		long double currCookies = 0;
		long double prevtimetoEnd = 1E30;
		
		long double currTime = 0;

		while(true)
		{
			//current rate how long till I can get next farm and increase my rate
			long double nextFarm = c / rate;
			//current rate how long till I get all the cookiess
			long double allcookies = x / rate;
			long double timeToEnd = currTime + allcookies;
			
			if(timeToEnd > prevtimetoEnd)	{break;}

			currTime += nextFarm;
			prevtimetoEnd = timeToEnd;
			rate += f;
		}

		printf("Case #%d: %.7Lf\n", cn, prevtimetoEnd);
		//cout << "Case #" << setprecision(7) << cn << ": " << prevtimetoEnd << endl;
	}
	return 0;
}
