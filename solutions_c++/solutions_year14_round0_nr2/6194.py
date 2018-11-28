#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;
int main(int argc, char** argv) {
	string line;
	ifstream infile (argv[1]);
	ofstream outfile ("output.txt");
	if (infile.is_open()) {
		int num_tests;
		infile >> num_tests;
		for (int i=0; i<num_tests; i++) {
			double cost, farm, target;
			infile >> cost >> farm >> target;
			// Base case
			double min_time = target / 2.0;
			double cur_time = cost / 2.0;
			double num_farms = 0.0;
			while(true) {
				num_farms++;
				double tmp_time = cur_time + (target / (2.0 + (farm * num_farms)));
				if (tmp_time < min_time) {
					min_time = tmp_time;
					cur_time += cost / (2.0 + (farm * num_farms));
				} else {
					outfile << "Case #" << i+1 << ": ";
					outfile << setprecision((int)(log10(min_time))+8) << min_time << endl;
					break;
				}
			}
		}
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file" << endl;
	
	return 0;
}