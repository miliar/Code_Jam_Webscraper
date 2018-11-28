#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	int T;
	double X,F,C,t0,t1,t3,F0;
	while ( ~scanf("%d",&T) )
	for ( int t = 1 ; t <= T ; ++ t ) {
		scanf("%lf%lf%lf",&C,&F,&X);
		if ( C < X ) {
			t3 = 0.0;
			F0 = 2.0;
			while ( C < X ) {
				t3 += C/F0;
				t0 = (X-C)/F0;
				t1 = X/(F0+F);
				if ( t0 < t1 ) break;
				F0 += F;
			}
			t3 += (X-C)/F0;
		}else t3 = X/2.0;
		printf("Case #%d: %.7lf\n",t,t3);
	}
	return 0;
}
