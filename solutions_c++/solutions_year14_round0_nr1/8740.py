// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main(int argc, char* argv[])
{
	int testCases = 0;
	int firstChoice = 0, secondChoice = 0;
	int firstChoiceRow[4] = { 0, 0, 0, 0 };
	int secondChoiceRow[4] = { 0, 0, 0, 0 };
	std::string tmpLine = "";
	std::string choiceLine = "";

	std::ifstream myfile("input.txt", std::ios::in);
	std::ofstream outFile("output.txt", std::ios::out);
	
	if (myfile.is_open() && outFile.is_open())
	{
		getline(myfile, tmpLine);
		testCases = stoi(tmpLine);

		for (int i = 0; i < testCases; i++)
		{
			int matchFound = 0;
			int theMatch = 0;

			/******first choice*******/
			getline(myfile, tmpLine);
			firstChoice = stoi(tmpLine);

			for (int i = 0; i < 4; i++)
			{
				if (i == (firstChoice-1))
				{
					getline(myfile, choiceLine);
				}
				else
				{
					getline(myfile, tmpLine);
				}
			}

			std::istringstream ss(choiceLine);
			int index = 0;
			while (4 != index)         // See the WARNING above for WHY we're doing this!
			{
				std::string x;               // here's a nice, empty string
				getline(ss, x, ' ');  // try to read the next field into it
				firstChoiceRow[index++] = stoi(x);
			}

			/****second choice*****/
			getline(myfile, tmpLine);
			secondChoice = stoi(tmpLine);

			for (int i = 0; i < 4; i++)
			{
				if (i == (secondChoice-1))
				{
					getline(myfile, choiceLine);
				}
				else
				{
					getline(myfile, tmpLine);
				}
			}

			std::istringstream ss2(choiceLine);
			index = 0;

			while (4 != index)         // See the WARNING above for WHY we're doing this!
			{
				std::string x;               // here's a nice, empty string
				getline(ss2, x, ' ');  // try to read the next field into it
				secondChoiceRow[index++] = stoi(x);
			}

			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (firstChoiceRow[i] == secondChoiceRow[j])
					{
						theMatch = firstChoiceRow[i];
						matchFound++;
					}
				}
			}

			if (1 > matchFound)
			{
				outFile << "Case #" << (i + 1) << ": Volunteer cheated!\n";
			}
			else if (1 < matchFound)
			{
				outFile << "Case #" << (i + 1) << ": Bad magician!\n";
			}
			else
			{
				outFile << "Case #" << (i + 1) << ": " << theMatch << "\n";
			}
			

		}

		myfile.close();
		outFile.close();
	}
	else std::cout << "Unable to open file";

	std::cin.get();
	return 0;
}