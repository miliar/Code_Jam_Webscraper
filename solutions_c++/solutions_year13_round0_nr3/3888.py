// ProCFairAndSquare.cpp -MysticBoy

#include <iostream>
#include <string>
#include <cmath>
//#include <cstdlib>
//#include <cstdio>

using namespace std;

int main(int cmdcount, char **cmdlist)
{
	int T; 			//number of test cases, T: 1 <= T <= 100
	int A, B;		//	1 ≤ N, M ≤ 1000

	int long i, j, k, l, m;

	// input
	cin >> T;
	int result[T+1];

	int FScnt = 0;


	for(k = 1; k <= T; ++k) {
		cin >> A >> B;

		//print input
		//cout << A <<" " << B << endl;
		
		FScnt = 0;
		for(i = A; i <= B; ++i) {
			int sqr = sqrt(i);
			if( i == sqr*sqr) { 
				//cout <<" i:" << i << "\t" << sqr << endl;
				int d = i;
				int r = 0;
				int nd = 0;
				while(d > 0) {
					r = d%10;
					d = d/10;
					nd = nd * 10 + r;
				}

				d = sqr;
				r = 0;
				int sqnd = 0;
				
				while(d > 0) {
					r = d%10;
					d = d/10;
					sqnd = sqnd * 10 + r;
				}
			
				
				if( nd == i && sqnd == sqr )
					++FScnt;

				//cout << "i: " << i << "     nd : " << nd <<"        FS Count : " << FScnt << endl;
						
			}
			//cout << "i : " << i <<"----------------------- "<< endl;
		}

		result[k] = FScnt;

	}	//End T loop


	//cout << "-------------------------" << endl;
	for(k = 1; k <= T; ++k) 
		cout <<"Case #"<< k <<": "<< result[k] << endl;
	/* */
	return 0;
}	//End main


