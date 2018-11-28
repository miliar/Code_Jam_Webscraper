#include <algorithm>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>


void main() {
	int i,j,T,Trun=1;
	int r,counter;
	float a,b,t,total,next;
	std::cin >> T;
	while (Trun <= T) {
		std::cin >> r >> t ;
		// printf ("r = %d\nt = %f\n",r,t);
		total = 0, counter = 0, next = 0;
		while ( total <= t ) {
			counter++; 
			a=r+2*counter-1;
			b=r+2*counter-2;
			total += a*a-b*b;
			// printf ("total = %f\n",total);
		}
		printf ("Case #%d: %d\n",Trun++, --counter);
	}

}

