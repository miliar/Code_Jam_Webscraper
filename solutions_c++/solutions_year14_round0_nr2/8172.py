#include<iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	cin>>T;
	for( int ii = 1; ii <= T; ++ii) {
		
		double c,f,x;
		cin>>c>>f>>x;
		double act_time = 0;
		double act_gain = 2, opt_time = 99999999.0;
		while(opt_time > act_time) {
			double new_time = act_time + x/act_gain;
			if( new_time < opt_time)
				opt_time = new_time;
			act_time += c/act_gain;
			act_gain += f;
		}
		printf("Case #%d: %.7lf\n", ii, opt_time);
	}

	return 0;
}