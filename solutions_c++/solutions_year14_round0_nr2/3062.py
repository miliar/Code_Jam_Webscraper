#include <cstdio>

using namespace std;

int main() {

	int T;
	scanf("%d", &T);
	
	for(int k = 1; k <= T; k++) {
		double min = 10000000.0;
	
		double C,F,X;
		double G = 2;
		
		scanf("%lf %lf %lf", &C, &F, &X);
		
		min = X/G;
		
		double time = 0.0;
		
		while(true) {
			time += C/G;
			G += F;
			double newtime = time + X/G;
			if(newtime <= min) {
				min = newtime;
			} else {
				break;
			}
		}
		
		printf("Case #%d: %.7lf\n", k, min);
	}
	
	return 0;
}
