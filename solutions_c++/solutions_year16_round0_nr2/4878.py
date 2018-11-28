//// Imports
#include <iostream>
#include <fstream>
#include <string>

//// Methods
bool allUp(char * theArray, int theSize)
{
	// check for upside down pancakes
	for (int i = 0; i < theSize; ++i)
	{
		if (theArray[i] == '-')
		{
			return false;
		}
	}
	// case: all up
	return true;
}

void flipStack(char * theArray, int theFlipPos)
{
	for (int i = 0; i <= theFlipPos; ++i)
	{
		if (theArray[i] == '-')
		{
			theArray[i] = '+';
		}
		else
		{
			theArray[i] = '-';
		}
	}
}

//// Driver
int main ()
{
	// initialize
	std::ifstream ifs("data.in");
	std::ofstream ofs("data.out");
	int iCasesCount = 0;
	std::string sLine = "";
	char iCase = 0;
	// read in Cases
	ifs >> iCasesCount;
	std::cout << "\n[Question 2]\n"; 
	std::cout << " - Number of Cases: "<< iCasesCount << '\n';
	std::cout << " - Processing ... ";
	// process line bl line
	for (int i = 1; i <= iCasesCount; ++i)
	{
		// initalize
		ofs << "Case #" << i << ": ";
		char * stack = new char[100];
		ifs >> sLine;
		int iSize = sLine.size();
		// read in
		for (int j = 0; j < iSize; ++j)
		{
			stack[j] = sLine[j];
		}
		// flipping
		int iFlips = 0;
		while (allUp(stack,iSize) == false)
		{
			// check from bottom up
			for (int j = iSize - 1; j >= 0; --j)
			{
				if (stack[j] == '-')
				{
					flipStack(stack,j);
					iFlips++;
					break;
				}
			}
		}
		// report
		ofs << iFlips << '\n';
		// cleanup
		delete [] stack;
		
	}
	std::cout << "[Done]\n";
	// clean-up
	ifs.close();
	ofs.close();
}