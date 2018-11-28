#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#include <cstdlib>

using namespace std;

class OminousOmino {
public:


	string Compute(int X, int R, int C) {
		
	
		if (X == 1 || (X == 2 && (R*C) % 2 == 0) || (X == 3 && (R*C == 9 || R*C == 12 || R*C==6)) || (X==4 && (R*C==16 || R*C==12)))
		return "GABRIEL";

		return "RICHARD";
	}
};

int main(int argc, char *argv[]) {
	
	ifstream inFile("C:\\Users\\Mike\\Downloads\\D-small-attempt0.in");
	ofstream outFile("C:\\Users\\Mike\\Downloads\\D-small-attempt0.out");
	string line;
	getline(inFile, line);
	int cases;
	istringstream(line) >> cases;
	OminousOmino proc;
	for (int n = 0; n < cases; n++){
		string nums;
		int X, R, C;
		getline(inFile, nums);
		istringstream iss(nums);
		iss >> X >> R >> C;

		string ret = proc.Compute(X, R, C);
		outFile << "Case #" << (n + 1) << ": " << ret << "\n";
	}
	return 0;
}

