#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <streambuf>
#include <cstdint>
#include <assert.h>
#include <set>
#include <iomanip>


int main() {

	int n;
	std::cin >> n;

	for(int _n=0; _n<n; ++_n) {
		std::cout << "Case #" << (_n+1) << ": ";

		double c, f, x;
		std::cin >> c >> f >> x;

		double prod = 2.0;

		double t, tb, ot = 0.0; 
		
		while(1) {		
			t = x / prod;
			tb = (c / prod) + x / (prod + f);
			if(tb < t) {
				ot += (c / prod);
				prod += f;
			}
			else {
				break;
			}
		}
		std::cout << std::fixed << std::setprecision(7) << (ot+t) << std::endl;
	}

	return 0;
}