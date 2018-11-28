#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	ifstream inputFile("D-small-attempt0.in");
	ofstream outputFile("output.txt");

	int testNumber = 0;

	inputFile >> testNumber;

	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": " ;
		int k, c, s;

		inputFile >> k;
		inputFile >> c;
		inputFile >> s;

		for (int i = 1; i <= k; ++i)
		{
			outputFile << i << " ";
		}
		outputFile << endl;
		
	}

	return 0;
}
