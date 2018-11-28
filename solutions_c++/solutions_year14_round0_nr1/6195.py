#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main(int argc, char** argv) {
	string line;
	ifstream infile (argv[1]);
	ofstream outfile ("output.txt");
	if (infile.is_open()) {
		int num_tests;
		infile >> num_tests;
		for (int i=0; i<num_tests; i++) {
			int row_idx;
			int tmp_val;
			infile >> row_idx;
			int* first_row;
			int* second_row;
			for (int j=0; j<4; j++) {
				for (int k=0; k<4; k++) {
					if (j == row_idx-1) {
						infile >> first_row[k];
					} else {
						infile >> tmp_val;
					}
				}
			}
			infile >> row_idx;
			for (int j=0; j<4; j++) {
				for (int k=0; k<4; k++) {
					if (j == row_idx-1) {
						infile >> second_row[k];
					} else {
						infile >> tmp_val;
					}
				}
			}

			// Find out how many in the first row are also in 
			// the second row
			int num_matches = 0;
			int match = 0;
			for (int j=0; j<4; j++) {
				for (int k=0; k<4; k++) {
					if (first_row[j] == second_row[k]) {
						num_matches++;
						match = first_row[j];
					}
				}
			}
			outfile << "Case #" << i+1 << ": ";
			if (num_matches == 0) { 
				outfile << "Volunteer cheated!" << endl; 
			} else if (num_matches == 1) {
				outfile << match << endl;
			} else {
				outfile << "Bad magician!" << endl;
			}
		}
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file" << endl;
	
	return 0;
}