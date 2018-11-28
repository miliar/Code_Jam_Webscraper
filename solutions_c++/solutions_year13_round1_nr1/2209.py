#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>

#define BUFLEN 5
#define RESLEN 5000

using namespace std;

int main(){
	int T, case_num;
	cin >> T;
	for (case_num = 1; case_num <= T; ++case_num){
		unsigned long long r, t;
		cin >> r >> t;
		// Calculate 1/2(r)(r-1)
		double inner_area = 0.5*((double)r)*((double)(r-1));
		//printf("%lf\n", inner_area);
		double y = ((double)t + inner_area)*2;
		double x = (sqrt(1+4*y)-1)/2;
		//printf("%lf\n", x);
		unsigned long long n = (unsigned long long)floor(x);
		unsigned long long result = n, rez;
		//printf("\n%lld\n", result);
		if (r % 2 == 0){ // r is even, then result must be odd
			if (result % 2 == 0)
				result -= 1;
			//rez = (result-r-1)/2;
		} else{ //r is odd, then result must be even
			if (result % 2 != 0)
				result -= 1;
			//rez = (result-r+1)/2;
		}
		//if (rez == 0) rez = 1;
		rez = (result-r+1)/2;
		//printf("\n%lld\n", result);
		cout << "Case #" << case_num << ": " << rez << endl;
	}
	return 0;
}

