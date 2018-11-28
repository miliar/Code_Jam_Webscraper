#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for ( int b = 1; b <= t; b++ ) {
		
		float c, f, x;
		
		cin >> c >> f >> x;

		double rate = 2;
		double target = 0;
		double t_time = 0;

		while ( target != x ) {
			double t1 = (x - target)/ rate;
			double t2 = c/rate + (x - target)/(rate + f);
			
			if ( t2 < t1) {
				t_time += c/rate;
				rate += f;
			} else {
				printf("Case #%d: %.7f\n",b, t_time+t1);
				break;
			}
		}
	}

	return 0;
}
				

				 

		

