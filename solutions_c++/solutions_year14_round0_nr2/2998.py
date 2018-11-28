#include <iostream>
#include <cstdio>

using namespace std;

double calculateTime(double farmCost, double extraCookiesPerSecond, double minimumLimit )
{
	/*
	 * Logic
	 */
	double cookiesCount = 0;
	double cookiesPerSecond = 2; // Initial cookies production rate

	double time1, time2, totalTime;
	double prevTime, currTime;
	totalTime = 0;

	/*
	 * First we will calculate time required to reach the minimumLimit of left over cookies
	 */
	time1 = totalTime + (minimumLimit/cookiesPerSecond);
	prevTime = time1;

	/*
	 * Second we will calculate minimum time required to buy farm
	 */
	time2 = totalTime + (farmCost/cookiesPerSecond);
	totalTime = time2;
	cookiesPerSecond += extraCookiesPerSecond;
	
	while(true) {
		time1 = totalTime + (minimumLimit/cookiesPerSecond);
		currTime = time1;
		
		if( prevTime < currTime )
			break;
		
		prevTime = currTime;
		
		time2 = totalTime + (farmCost/cookiesPerSecond);
		totalTime = time2;
		cookiesPerSecond += extraCookiesPerSecond;
	}
	
	return prevTime;
}

int main()
{
	int T;
	double C, F, X;
	double time;

	scanf("%d",&T);
	for( int i = 1; i <= T; i ++ ) {
		/*
		 * Reading User Input
		 */
		scanf("%lf %lf %lf", &C, &F, &X);
		time = calculateTime( C, F, X );
		printf("Case #%d: %lf\n", i, time);
	}

	return 0;
}
