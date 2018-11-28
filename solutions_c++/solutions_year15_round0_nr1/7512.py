#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int testCases = 0;
	int numberOfPeople;
	string people;
	int numToAdd = 0;
	int peopleCounter = 0;

	ifstream input("A-large.in", ios::in);
	ofstream output("output.txt", ios::out);

	input >> testCases;
	input.ignore();


	for (int i = 1; i <= testCases; i++)
	{
		peopleCounter = 0;
		numToAdd = 0;
		input >> numberOfPeople;
		input >> people;
		for (int j = 0; j < numberOfPeople+1; j++)
		{
			if ((people[j] - '0') != 0)
			{
				peopleCounter += (people[j] -'0');
			}
			else
			{
				if (j == 0)
				{
					numToAdd++;
					peopleCounter++;
				}
				else if (peopleCounter <= j)
				{
					while (peopleCounter <= j)
					{
						numToAdd++;
						peopleCounter++;
					}
				}
			}
		}
		output << "Case #" << i << ": " << numToAdd << "\n";
	}

	return 0;
}