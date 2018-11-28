#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	scanf("%d", &t);
	double C,F,X;
	for (int k = 1 ; k <= t ; k++) {
		scanf("%lf%lf%lf", &C,&F,&X);
		
		double time1,time2,time = 0.00;
		
		double rate = 2;
		
		while(1) {
			time1 = time + (X/(rate*1.0));
			time2 = time + (C/(rate*1.0)) + (X/(rate*1.0+F*1.0));
			
			
			if (time2 < time1) {
				
				time = time + (C/(rate*1.0));
				rate  = rate + F;
			
			} else {
				time = time1;
				break;
			}
		}
		printf("Case #%d: %0.7lf\n",k,time);
	}
	return 0;
}
