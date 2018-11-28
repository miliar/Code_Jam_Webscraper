#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define uint	unsigned int

#define CHAR_TO_INT(C)	((C) - '0')

int main()
{
	uint nbTests;
	cin >> nbTests;
	for (uint testId = 0; testId < nbTests; testId++)
	{
		uint Smax;
		cin >> Smax;
		vector<uint> shyPeople(Smax + 1, 0);
		string shyDataStr;
		getline(cin, shyDataStr);
		for (uint i = 1; i < shyDataStr.size(); i++)
			shyPeople[i - 1] = CHAR_TO_INT(shyDataStr[i]);	// Attention à l'espace en début de chaîne

		uint nbPeopleUp = 0;
		uint nbPeopleAdded = 0;
		for (uint shyLevel = 0; shyLevel <= Smax; shyLevel++)
		{
			if (nbPeopleUp < shyLevel)
			{
				uint addedPeople = (shyLevel - nbPeopleUp);
				nbPeopleAdded += addedPeople;
				nbPeopleUp += addedPeople;
			}
			nbPeopleUp += shyPeople[shyLevel];
		}
		cout << "Case #" << testId + 1 << ": " << nbPeopleAdded << endl;
	}

	return EXIT_SUCCESS;
}
