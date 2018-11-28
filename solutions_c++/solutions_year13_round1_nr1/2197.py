#include "math.h"
#include "stdio.h"

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

typedef long long int int64;

int main(int argc, char *argv[])
{
	size_t T, count = 1;
	string line;

	// get T
	getline(cin, line);
	stringstream(line) >> T;

	// get all cases and process it
	for(size_t count = 1; count <= T; count++) {

		int64 r, t;
		int64 N = 0;
		int64 sum = 0;

		// get r, t
		getline(cin, line);
		stringstream(line) >> r >> t;
		// cout << "r: " << r << ", t: " << t << endl;

		while (1) {
			sum = 2*N*N+(2*r+3)*N+(2*r+1);
			if (sum > t)
				break;
			else
				N++;
		}
		cout << "Case #" << count << ": " << N << endl;
	}

	// int64 a = 2;
	// int64 b = 2*r + 3;
	// int64 c = 2*r + 1 - t;

	// double discriminant = (pow(b,2) - 4*a*c);
	// double positive_root = (((-b) + sqrt(discriminant))/(2*a));
	// double negative_root = (((-b) - sqrt(discriminant))/(2*a));

	// //Output
	// if (discriminant == 0)
	// {
	// cout << "\n\nThe discriminant is ";
	// cout << discriminant << endl;
	// cout << "The equation has a single root.\n\n";
	// }
	// else if (discriminant < 0)
	// {
	// cout << "\n\nThe discriminant is ";
	// cout << discriminant << endl;
	// cout << "The equation has two complex roots.\n\n";
	// }
	// else
	// {
	// cout << "\n\nThe discriminant is ";
	// cout << discriminant << endl;
	// cout << "The equation has two real roots.\n\n";
	// }

	// cout << negative_root << endl << positive_root << endl;

	return 0;
}