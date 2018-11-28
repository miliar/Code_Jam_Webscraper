#include <iostream>
#include <iomanip>
using namespace std;

int main(){

	int TestCases;
	cin >> TestCases;

	for (int test=1; test<=TestCases; test++){
		double C, F, X;
		cin >> C >> F >> X;

		double x = 0, r = 2, t = 0, T = C/F;
		
		cout.setf( ios::fixed );
		cout.precision( 7 );
		
		double dx;
		// C < X
		while(1){
			
			//cout << "t=" << t << ":\t" << x << "\t@" << r << "\t";

			if ( (dx = X - x) < 1E-7 ) break;

			if( x < C) {
				if( X < C ){
					x = X;
					t += X / r;
				}else{
					t += C / r;
					x = C;
				}
			}else{	// can afford
				if( T * r >= dx ){ //no need to buy
					//cout << "don't buy";
					t += dx / r;
					x += dx;
				}else{
					//cout << "buy";
					r += F;
					t += C/r;
				}
			}
			//cout << "\n";
		}

		//cout << "\n";
		cout << "Case #" << test << ": " << t << "\n";

	}

}
