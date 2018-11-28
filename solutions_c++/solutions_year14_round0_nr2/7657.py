#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int main ()
{
	int no_testcases;
	scanf("%d", &no_testcases);
	
	
	for (int i=1; i<=no_testcases; i++) {
		double C, F, X;
		scanf("%lf",&C);   //Cost of farm
		scanf("%lf",&F);   //Increment
		scanf("%lf",&X);  //target
		//inital cookie rate  = 2

		//continue to produce cookie at a given rate (2+r*F) if  
		// X/(2+r*F)  <= X/(2+(r+1)*F) + C/(2+r*F)

		// int R = ceil((F*X-F*C-2*C)/(F*C));  // We will buy R farms
		// printf("R = %d\n", R);
		double time_sum = 0;
		if (C>=X)
		{
			printf("Case #%d: %lf\n",i, X/2);
			continue;
		}
		for (int j = 0; j < X; ++j)
		{
			double time1 = X/(2+j*F);
			double time2 = C/(2+j*F) + X/(2+j*F+F);
			//we have j farms
			if(time1<time2){
				time_sum+= time1;
				break;
			}
			else{
				time_sum+= C/(2+j*F);
			}
			
		}
		printf("Case #%d: %lf\n",i, time_sum );
	}
	
	return 0;
}