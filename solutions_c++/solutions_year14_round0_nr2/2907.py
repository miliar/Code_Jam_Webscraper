#include <iostream>
#include <algorithm>
#include <math.h>
#include <cstdio>

using namespace std;

int main() {
	int tc;
	double C, X, F;
	double f_soln, f, time;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		cin>>C>>F>>X;

		f_soln = (X-C)*F/C;

		f = 2, time = 0;
		if (f_soln>f){
			time+= (C/f);
			while(f+F < f_soln){
				f+=F;
				time += (C/f);
			}
			f+=F;
		}
		time+=(X/f);
		printf("Case #%d: %.7f\n",t,time);
	}
	return 0;
}

