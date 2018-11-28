#include <cstdio>

using namespace std;

int main() {

	int T;
	long double C, F, X;
	scanf("%d ", &T);
	for(int t=0; t<T; t++) {
		printf("Case #%d:", t+1);
		
		scanf("%Lf %Lf %Lf ", &C, &F, &X);
		

		long double tmin = X / 2.0;
		long double a = 0.0;
		long double i = 2;
		//printf("bei null mal: %lf\n", tmin);
		int x=1;
		while(true) {
			a += C / i;
			i += F;
			if(a + X/i <= tmin) {
				//printf("%d mal: %lf\n", x++, tmin);
				tmin = a + X/i;
			} else {
				break;
			}
		}
		printf(" %.8Lf\n", tmin); 
			
	}

	return 0;
}
