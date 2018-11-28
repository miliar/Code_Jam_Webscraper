#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream inFile;
	ofstream outFile;
	char inputFileName[] = "C:\\Users\\Andrew\\Downloads\\A-large.IN";
	char outputFileName[] = "C:\\Users\\Andrew\\Downloads\\A-largeOut1.txt";

	inFile.open(inputFileName, ios::in);
	if (!inFile)
	{
		cerr << "Can't open input file " << inputFileName << endl;
		exit(1);
	}

	outFile.open(outputFileName, ios::out);
	if (!outFile)
	{
		cerr << "Can't open input file " << outputFileName << endl;
		exit(1);
	}

	int NUM_CASES;
	inFile >> NUM_CASES;

	for (int c = 1; c <= NUM_CASES + 1; c++)
	{
		int friends = 0;
		int maxShy;
		string audience;
		inFile >> maxShy >> audience;

		int standingCount = 0;
		for (int shyLevel = 0; shyLevel <= maxShy; shyLevel++)
		{
			standingCount += audience[shyLevel] - 48;

			while (standingCount < (shyLevel + 1))
			{
				friends++;
				standingCount++;
			}
		}

		if (c <= NUM_CASES)
			outFile << "Case #" << c << ": " << friends << endl;
	}

	inFile.close();
	outFile.close();

	return 0;
}