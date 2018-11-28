#include<iostream>
#include<fstream>
#include<ios>
#include<sstream>

using namespace std;

int main() {

	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int T;

	int i = 0;
	for (std::string line; std::getline(infile, line); i++) {
		std::istringstream iss(line);
		if (i == 0) {
			iss >> T;
		}
		else {
			int totalneed = 0;
			int totalstanding = 0;
			int length;
			iss >> length;
			length += 1;

			int * array;
			array = new int[length];

			int j = -1;
			for (char c; iss.get(c); j++){
				if (j == -1) {
					continue;
				}
				else {
					int resint = c - 48;
					array[j] = resint;
				}
			}

			for (int k = 0; k <= length - 1; k++) {
				//cout << array[k] << endl;
				if (k > totalstanding) {
					totalneed += (k - totalstanding);
					totalstanding = k;
				}
				totalstanding += array[k];
			}

			outfile << "Case #" << i << ": " << totalneed << endl;
		}
	}

}