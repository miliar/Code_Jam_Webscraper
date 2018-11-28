// cookie-clicker-alpha.cpp: Jagermeister
// Description: GCJ Qualification Round 2014 - B

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <fstream>

using namespace std;

int main() {
	int T;
	double C, F, X;

	double num_secs_x_now;
	double num_secs_x_plus_f;

	int farms;
	//double production = 0.0;
	//double production_plus_one = 0.0;

	bool done;

	ifstream input("C:\\Users\\mmatarazzo\\Downloads\\B-large.in");
	ofstream output("C:\\Users\\mmatarazzo\\Downloads\\B-large.out");

	input >> T;

	for (int i = 0; i < T; i++) {
		input >> fixed >> setprecision(7) >> C >> F >> X;
		//cout << fixed << setprecision(7) << C << endl << F << endl << X << endl;

		//cout << endl << i+1 << endl;
		
		farms = 1;
		done = false;

		num_secs_x_now = 0.0;
		//num_secs_x_plus_f = 0.0;

		num_secs_x_now = (double) (X / ((F*(farms-1)) + 2.0));
		//cout << num_secs_x_now << endl;
		while (!done) {
			//production = (4.0*farms) + 2.0;
			//production_plus_one = (4.0*farms+1) + 2.0;

			//num_secs_x_now = farms*(C / production) + (X / production);
			//num_secs_x_plus_f = (farms+1)*(C / production) + (X / production_plus_one);

			num_secs_x_plus_f = 0.0;

			for (int j = farms; j > 0; j--) {
				//num_secs_x_plus_f += (j)*(C / ((4.0*(j-1)) + 2.0));
				num_secs_x_plus_f += (double) ( C / ( (F* (j-1)) + 2.0) );
				//cout << num_secs_x_plus_f << endl;
			}
			num_secs_x_plus_f += (double) (X / ((F*farms) + 2.0) );
			//cout << num_secs_x_plus_f << endl;

			if (num_secs_x_now < num_secs_x_plus_f) done = true;
			else {
				farms++;
				num_secs_x_now = num_secs_x_plus_f;
				//cout << num_secs_x_now << endl;
			}
		}

		output << "Case #" << i+1 << ": " << fixed << setprecision(7) << num_secs_x_now << endl;
	}

	return 0;
}