#include <stdio.h>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++){
		double r = 2.0;
		double C, F, X;
		scanf("%lf %lf %lf ", &C, &F, &X);
		double time = 0;
		double time_min = X/r;
		
		time += C/r;
		r += F;
		//printf ("%lf %lf\n", time, r);
		
		while (time + X/r < time_min){
			time_min = time + X/r;
			time += C/r;
			r += F;
			//printf ("%lf %lf\n", time, r);
		}
		/*int farme = int (X/C);
		int f = 0;
		if (farme <= 1) time = X/r;
		else{
			farme--;
			while (f<farme){
				time += C/r; //time to buy farm
				r += F;
				f++;
			}
			time += X/r;
		}*/
		
		printf("Case #%d: %.7lf\n", t+1, time_min);
	}
	return 0;
}