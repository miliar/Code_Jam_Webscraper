#include <iostream>
#include <math.h>

#define PI 3.14159265


using namespace std;

int main(){

	int T;
	cin >> T;

	int i, j, k;

	for (i=1;i<=T;i++){
		long double r, t;
		cin >> r >> t;
/*
		long long count = 0;
		while (t > 0){
			t = t - (2*r + 1);
			if (t>=0){
				count ++;
				r = r + 2;
			}
		}	
*/
		long double c2 = floor( (sqrt((2*r-1) * (2*r-1) + 8 * t) - (2*r-1))/4);
		cout << "Case #" << i << ": " << c2 << endl;
	}

return 0;
}
