#include <cstdio>

using namespace std;

double farmCost, farmProd, goal;

int main () {

	int numCases;
	double maxTime, bestTime;

	scanf("%d", &numCases);
	for ( int cc = 1; cc <= numCases; ++cc ) {
		scanf("%lf %lf %lf", &farmCost, &farmProd, &goal);
		
		bestTime = maxTime = goal / 2.0; //never takes more than this, no factories bought
		
		int factories = 0;
		double production = 2.0;
		double timePassed = 0;
		while ( timePassed < bestTime ) {
			//wait to get factory
			timePassed += farmCost / production;
			// buy factory
			++factories;
			production += farmProd;
			// check if waiting now is best
			if ( timePassed + (goal / production) < bestTime ) {
				bestTime = timePassed + (goal / production);
			}
		}
		
		printf("Case #%d: %.7lf\n", cc, bestTime);		
		
	}
	
	return 0;
}
