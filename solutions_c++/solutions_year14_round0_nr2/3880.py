#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream input(argv[1]);
    size_t T, cc=0;
	long double C, F, X, init=2.00000000000;
	
	if(input >> T) {
		while(cc++ < T) {
			input >> C >> F >> X;

			long double m = X/C - (long double)2.0/F - (long double)1.0;
			if(m < 0) {
				cout << "Case #" << cc <<": " << X/init << endl;
			} else {
				long double l=0.00000000000, r=0.00000000000;
				int i;
								
				for(i=0; i<(int)m; i++) 
					l += C/(init + (long double)i*F);

				r = l + C/(init+(long double)i*F);

				l += X/(init + (long double)i*F);
				r += X/(init + (long double)(i+1)*F);
				cout << "Case #" << cc <<": " << setprecision(10) << min(l,r) << endl;
			}
		}		
	}

	return 0;
}
