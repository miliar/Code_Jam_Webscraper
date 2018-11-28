#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main(int argc, char** argv) {

	if (argc < 2) {
		cerr << "Usage: " << argv[0] << " input";
	}
	char gabriel[] = "GABRIEL";
	char richard[] = "RICHARD";
	
	ifstream fin(argv[1]);
	
	int ntests;
	fin >> ntests;
	for(int cs = 1; cs <= ntests; cs++) {
		int X, R, C, area;
		fin >> X >> R >> C;
		area = R*C;
		char const* result;
		if (X == 1) result = gabriel;
		else if (X == 2 && (area%2 == 0)) result = gabriel;
		else if (X == 3 && (area%3 == 0) && (R > 1 && C > 1)) result = gabriel;
		else if (X == 4 && (area%4 == 0) && (R > 2 && C > 2)) result = gabriel;
		else result = richard;
	
		cout << "Case #" << cs << ": " << result << endl;
	}
	
	return 0;
}