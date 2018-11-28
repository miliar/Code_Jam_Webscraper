#include <iostream>
#include <fstream>
#include <istream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>

std::string inFile = "magictrick.in.txt";
std::string outFile = "magictrick.out.txt";

std::ifstream iFile(inFile.c_str());
std::ofstream oFile(outFile.c_str());

void processInput(int choiceIndex, std::vector<int> & choice)
{
	std::vector<std::vector<int> > all_card_numbers;

	for (int j=1; j<=4; j++)
	{
		std::string line;
		std::getline(iFile, line);

		std::istringstream in(line);
		all_card_numbers.push_back(std::vector<int>(std::istream_iterator<int>(in), std::istream_iterator<int>()));
	}

	// save all elements corresponding to user choice
	choice = all_card_numbers[choiceIndex-1];
}

int readInt()
{
	int choice;

	std::string line;
	std::getline(iFile, line);

	std::istringstream in(line);
	if (!(in >> choice))
	{
		std::cout << "error while reading user choice" << std::endl;
		exit(1);
	}

	return choice;
}

int main()
{
	int t = readInt();

	for (int i = 1; i<=t; i++)
	{
		// user's first choice of row
		std::vector<int> choice1;
		int userChoice1 = readInt();
		processInput(userChoice1, choice1);

		// user's second choice of row
		std::vector<int> choice2;
		int userChoice2 = readInt();
		processInput(userChoice2, choice2);

		// guess user's chosen number
		std::sort(choice1.begin(), choice1.end());
		std::sort(choice2.begin(), choice2.end());

		std::vector<int> output;
		std::set_intersection(choice1.begin(), choice1.end(), choice2.begin(), choice2.end(), std::back_inserter(output));

		if (output.size() == 1)
		{
			for (std::vector<int>::const_iterator it = output.begin(); it != output.end(); it++)
			{
				oFile << "Case #" << i << ": " << *it << std::endl;
			}
		}
		else if (output.size() == 0)
		{
			oFile << "Case #" << i << ": Volunteer cheated!" << std::endl;
		}
		else
		{
			oFile << "Case #" << i << ": Bad magician!" << std::endl;
		}
	}

	oFile.close();
	iFile.close();
	return 0;
}
