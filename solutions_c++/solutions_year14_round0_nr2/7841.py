#include <iostream>
#include <algorithm>
#include <functional>
#include <iterator>
#include <string>
#include <bitset>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>

typedef long double real;
typedef long long unsigned lli;

const real defaultCookiePerSecond = 2.0;

real simulation(real C, real F, real X) {
	real min_time = 9999999999999.999;
	for(unsigned N = 0; true; ++N) {
		real time = 0.0;
		real cpc = defaultCookiePerSecond;
		
		unsigned n;
		for(n = 0; n<N; ++n) {
			time += C / cpc;
			cpc += F;
		}
		
		time += X / cpc;
		
		if(min_time > time) {
			min_time = time;
		} else {
			break;
		}
	}
	
	return min_time;
}

int main(void) {
	unsigned T;
	std::cin >> T;
	
	for(unsigned t=0; t<T; ++t) {
		real C, F, X;
		std::cin >> C >> F >> X;
		
		real R = simulation(C, F, X);
		
		std::cout << "Case #" << (t+1) << ": ";
		::printf("%.7Lf", R);
		std::cout << std::endl;
	}
	
	return 0;
}
