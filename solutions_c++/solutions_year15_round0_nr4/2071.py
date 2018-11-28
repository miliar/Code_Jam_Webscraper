#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
ofstream outFile("D-small-attempt0.out");
ifstream inFile("D-small-attempt0.in");


int T;
int X, R, C;
int main()
{
	inFile >> T;
	bool Output = false;
	for (int testcase = 0; testcase < T; testcase++){
		Output = false;
		inFile >> X >> R >> C;
		if (X == 1)
			Output = true;
		else if (X == 2 && (((R*C) % 2) == 0))
			Output = true;
		else if (X == 3 && (((R*C) % 3) == 0) && (R >= 2) && (C >= 2))
			Output = true;
		else if (X == 4 && (((R*C) % 4) == 0) && (R >= 3) && (C >= 3))
			Output = true;

		outFile << "Case #" << testcase + 1 << ": ";
		if ( Output )
			outFile << "GABRIEL" << endl;
		else
			outFile << "RICHARD" << endl;
	}
	outFile.close();
	return 0;
}
