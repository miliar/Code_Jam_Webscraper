/* scanf example */
#include <stdio.h>

int main ()
{ 
	int t; 
	double C; 
	double F; 
	double X; 
	double result = 0.00003;
	scanf ("%d",&t);
	for (int i = 0; i < t; ++i)
	{
		scanf ("%lf",&C);
		scanf ("%lf",&F);
		scanf ("%lf",&X);
		double tp = 0;
		double rate = 2;
		double prodtime = X/rate;
		result = tp+prodtime;
		while (true){
			if(prodtime>C/rate){
				tp += C/rate;
				rate += F;
				prodtime = X/rate;
				if(result > tp+prodtime){
					result = tp+prodtime;
				}else{
					break;
				}
			}else{
				break;
			}
		}
		 
		printf ("Case #%d: %.7lf\n",i+1, result);

	}
	
	return 0;
}
