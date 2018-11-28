#include<fstream>
#include<iomanip>
using namespace std;

int main() {
	ifstream fin("input.in");
	ofstream fout("output.out");
	int t, it;
	bool stop;
	double c, f, x, sum, current_rate;
	fout << setprecision(7);
	fout << fixed;
	fin >> t;
	for(it = 1; it <= t; it++) {
		fin >> c >> f >> x;
		current_rate = 2;
		sum = 0;
		stop = false;

		if(x < c) {
			sum = x / 2;
		} else {
			do {
				// get c cookies for a new farm
				sum += c / current_rate;
				// how to get x cookies faster - continuing or buying a new farm?
				if((x - c) / current_rate < x / (current_rate + f)) {
					// continue with the same current rate
					sum += (x - c) / current_rate;
					stop = true;
				} else {
					// buy a new farm and increase the current_rate
					current_rate += f;
				}
			} while(stop == false);
		}
		fout << "Case #" << it << ": " << sum << "\n";
	}
	return 0;
}
