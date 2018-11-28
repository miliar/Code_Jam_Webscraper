#include <iostream>
#include <fstream>

int main() {
	std::ifstream f("A-small-attempt0.in");	// open the file to read in data
	if (!f) {
		std::cerr << "Error: Failed to open." << std::endl;
		return -1;
	}

	std::ofstream myfile;
  	myfile.open ("output.txt");

	int nCase; // number of cases
	f >> nCase;
	int i;

	for (i = 0; i < nCase ; i++) {
		int answer1;
		int answer2;
		int grid1[16];
		int grid2[16];
		int count = 0;
		int result = 0;
		int j,k;


		f >> answer1;
		for (j = 0; j < 16; j++) f >> grid1[j];

		f >> answer2;
		for (j = 0; j < 16; j++) f >> grid2[j];

		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				if(grid2[(answer2-1)*4+j] == grid1[(answer1-1)*4+k]) {
					result = grid2[(answer2-1)*4+j];
					count++;
				}
			}
		}


		if(count == 0) myfile << "Case #" << i+1 << ": Volunteer cheated!" << std::endl;
		else if(count == 1) myfile << "Case #" << i+1 << ": " << result << std::endl;
		else myfile << "Case #" << i+1 << ": Bad magician!" << std::endl;


	}
	return 0;



}