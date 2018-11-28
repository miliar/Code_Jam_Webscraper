#include <map>
#include <Windows.h>
#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

std::map<int, bool> SeenNumbers;

int numDigits(int number)
{
	int digits = 0;
	if (number < 0) digits = 1;
	while (number) {
		number /= 10;
		digits++;
	}
	return digits;
}

bool CheckNumber(int num)
{
	int iNums = num;
	int iNumsSize = numDigits(num);
	for (int i = iNumsSize - 1; i >= 0; i--) {
		int y = pow(10, i);
		int z = iNums / y;
		int x2 = iNums / (y * 10);

		int a = z - x2 * 10;

		if (!SeenNumbers[a])
		{
			SeenNumbers[a] = true;
		}

		if (SeenNumbers[0] && SeenNumbers[1] && SeenNumbers[2] && SeenNumbers[3] && SeenNumbers[4] && SeenNumbers[5] && SeenNumbers[6] && SeenNumbers[7] && SeenNumbers[8] && SeenNumbers[9])
		{
			return true;
		}
	}

	return false;
}

int main()
{
	int caseI = 0;
	bool set = false;
	std::string line;
	std::ifstream infile("A-large.in");
	ofstream outputFile;
	outputFile.open("output.txt");
	while (std::getline(infile, line))
	{

		if (caseI == 0)
		{
			caseI = 1;
		}
		else
		{
			if (caseI == 1 && !set)
			{
				caseI = 0;
				set = true;
			}
			caseI = caseI + 1;
			int numb;
			istringstream(line) >> numb;
			int startingNumber = numb;
			int currentNumber = 1;
			int storage;
			int ready = true;
			while (ready)
			{
				if (startingNumber == 0)
				{
					outputFile << "Case #" << caseI << ": " << "INSOMNIA" << std::endl;
					ready = false;
					SeenNumbers.clear();
				}
				storage = startingNumber * currentNumber;
				currentNumber = currentNumber + 1;
				if (CheckNumber(storage))
				{
					outputFile << "Case #" << caseI << ": " << storage << std::endl;
					ready = false;
					SeenNumbers.clear();
				}
			}
		}
	}

	outputFile.close();

	return 1;
}