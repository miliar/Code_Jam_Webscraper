#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>
#include <cstdlib>

using namespace std;


int main() {
	int cases=0;
	cin >> cases;
		
	for(int casesIter=0;casesIter<cases;casesIter++) {
		long double  farmCost, farmProduceRate, targetCookies, balance = 0, currentRate = 2, time = 0;

		scanf("%Lf %Lf %Lf\n", &farmCost, &farmProduceRate, &targetCookies);
		
		while((targetCookies/currentRate) > ( (farmCost/currentRate) + (targetCookies/(currentRate+farmProduceRate))) ) {
			time += (farmCost/currentRate);
			currentRate += farmProduceRate;
		}
		
		time += (targetCookies/currentRate);
		
		printf("Case #%d: %.7Lf\n",casesIter+1, time);
		
	}
	
	return 0;
}