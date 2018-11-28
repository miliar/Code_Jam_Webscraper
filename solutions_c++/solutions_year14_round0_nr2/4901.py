#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	int currentCase = 0;
	while(T--) {
		currentCase++;
		double C, F, X, previous = -1.0f, current = 0.0f;
		scanf("%lf %lf %lf", &C, &F, &X);
		for(int i=0; ; i++) {
			double timeToBuyFarm = 0.0f;
			for(int j=0; j<i; j++) {
				timeToBuyFarm += ( C/( 2.0 + (j*F) ) );
			}
			current = timeToBuyFarm + (X / ( 2.0 + (i * F)));
			if(i == 0) {
				previous = current;
			}
			if(previous < current) {
				break;
			}
			previous = current;
		}
		
		printf("Case #%d: %.7lf\n", currentCase, previous);
	}
	return 0;
}