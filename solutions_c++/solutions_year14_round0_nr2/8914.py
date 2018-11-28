#include <cstdio>

int main() {
	int numberOfTestCases;
	double cost,rate,goal,secondsCounter,currentRate,currentCookies;
	scanf("%i",&numberOfTestCases);
	for (int i = 1; i < numberOfTestCases + 1; ++i) {
		currentRate = 2;
		scanf("%lf%lf%lf",&cost,&rate,&goal);
		secondsCounter = cost/currentRate;
		currentCookies = secondsCounter*currentRate;
		while ( true ) {
			if ( (goal-currentCookies)/currentRate <= (goal)/(currentRate+rate) )
				break;	
			else {
				currentRate += rate;
				secondsCounter += (cost)/currentRate;
			}		
		}
		secondsCounter += (goal-currentCookies)/currentRate;
		printf("Case #%i: %.7lf\n",i,secondsCounter);
	}
	return 0;
}