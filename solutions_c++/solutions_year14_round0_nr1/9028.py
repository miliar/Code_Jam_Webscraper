#include <iostream>
using namespace std;
#include "constants.h"

int main(int argc, char* argv[])
{
	string inputFile(testCase);
	string outputFile(testCase);
	inputFile  += ".in";
	outputFile  += ".out";

	freopen(inputFile.c_str(), "r", stdin);
	freopen(inputFile.c_str(), "r", stdout);

	int T;
	cin >> T;

	cout << T << " Cases to follow!" << endl;

	return 0;
}
