//
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");
	int numCases;
	string pancakes, tempPancake;

	if (!inFile)
	{
		cout << "File not working" << endl;
		return 0;
	}

	inFile >> numCases;

	inFile.ignore();

	for (int i = 0; i < numCases; i++)
	{
		getline(inFile, pancakes);

		bool allHappy = false;
		int countSwaps = 0;
		int diff;

		outFile << "Case #" << i + 1 << ": ";

		while (!allHappy)
		{
			tempPancake = "";

			if (pancakes[0] == '-')
			{
				diff = pancakes.find("+");
				if (diff < 0)
				{
					diff = pancakes.length();
				}
			}
			else if (pancakes[0] == '+')
				diff = pancakes.find("-");

			if (diff < 0)
				allHappy = true;
			else
			{
				countSwaps++;
				tempPancake = pancakes.substr(0, diff);
				reverse(tempPancake.begin(), tempPancake.end());
				for (int j = 0; j < tempPancake.length(); j++)
				{
					if (tempPancake[j] == '+')
						pancakes[j] = '-';
					else if (tempPancake[j] == '-')
						pancakes[j] = '+';
				}

				if (pancakes[0] == '-')
				{
					diff = pancakes.find("+");
					if (diff < 0)
					{
						diff = pancakes.length();
					}
				}
				else if (pancakes[0] == '+')
					diff = pancakes.find("-");

				if (diff < 0)
					allHappy = true;
			}
		}

		outFile << countSwaps << endl;
	}

	return 0;
}