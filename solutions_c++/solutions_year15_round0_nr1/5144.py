#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
/*
 * MAIN FUNCTION
 */

std::string handleTestCase(std::string line);

int main(int argc, char *argv[]) {
	if (argc != 3) {
		std::cerr << "must include an input and output file!" << std::endl;
		return 1;
	}

	std::ifstream infile(argv[1]);
	std::ofstream outfile(argv[2]);
	
	if (!infile.is_open() || !outfile.is_open()) {
		std::cerr << "File I/O error!" << std::endl;
		return 2;
	}
	
	// get number of test cases
	std::string line;
	std::getline(infile, line);
	int testCases = atoi(line.c_str());

	// read the input file line by line
	for (int i = 0; i < testCases; ++i) {
		std::getline(infile, line);
		outfile << "Case #" << i + 1 << ": " << handleTestCase(line) << std::endl;
	}

	// clean up the I/O streams
	infile.close();
	outfile.flush();
	outfile.close();

	return 0;
}

int solveShyness(int *shynessVals, int maxShyness) {
	int friendsToInvite = 0;
	int audienceSize = 0;

	for (int i = 0; i <= maxShyness; ++i) {
		int someFriends = 0;
		while (i > (audienceSize + friendsToInvite)) {
			++friendsToInvite;
		}

		// update friends to invite
		friendsToInvite += someFriends;

		// update audienceSize
		audienceSize += shynessVals[i];
	}

	return friendsToInvite;
}

std::string handleTestCase(std::string line) {
	std::istringstream input(line.c_str());

	int maxShyness;
	std::string shynessString;

	input >> maxShyness >> shynessString;

	// make it an array
	int *shynessArr = new int[maxShyness + 1];

	// parse shyness values
	for (int i = 0; i < shynessString.size(); ++i) {
		std::string str = shynessString.substr(i, 1);
		shynessArr[i] = atoi(str.c_str());
	}

	std::stringstream ss;
	ss << solveShyness(shynessArr, maxShyness);
	delete[] shynessArr;

	return ss.str();
}