#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int maxPossibleNumber(int r, int t)
{
	unsigned int multiplier = 0, count = 0;

	do
	{
		t -= (2*r + multiplier*4 + 1);
		count++;
		multiplier++;
	}
	while(t>=0);

	if (count <= 0)
	{
		return 0;
	}

	return count-1;
}

int main()
{
	unsigned int r, t;

	ifstream inputFile;
	inputFile.open("A-small-attempt0.in");
	if ( inputFile.good() )
	{
		unsigned int numberOfInputs;
		inputFile >> numberOfInputs;

		for(unsigned int inputNumber=0; inputNumber<numberOfInputs;)
		{
			if (inputFile >> r >> t)
			{
				cout << "Case #" << ++inputNumber << ": " << maxPossibleNumber(r, t) << endl;
			}
		}
	}
	inputFile.close();

	return 0;
}
