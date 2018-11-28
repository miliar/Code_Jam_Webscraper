#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

int main (void)
{
	int T; 		// number of games
	double C; 	// factory cost
	double F;	// factory speedup
	double X;	// end of the game
	
	double rate;
	double time;
	
	cin >> T;
	
	for (int t = 0; t < T; t++) {

		// read input
		cin >> C;
		cin >> F;
		cin >> X;
		
		time = 0.0;
		rate = 2.0;
	
		while (1) {

			if (X/rate < C/rate + X/(rate + F)) {
				//beter to just wait
				time += X/rate;
				break;
			} else {
				// better to buy factory
				time += C/rate;
				rate += F;
			}
		}
	
		// Output
		cout << fixed;
		cout << setprecision(7) << "Case #" << t+1 << ": " << time << endl;		
	}
		
	return 0;	
}
			