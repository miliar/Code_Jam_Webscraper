#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

void main(int argc, char* argv)
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int maxS;
		cin >> maxS;
		
		string audience;
		cin >> audience;

		vector<int> shynessLevels;
		for (int i = 0; i < maxS+1; i++)
		{
			char c = audience[i];
			int value = atoi(&c);
			shynessLevels.push_back(value);
		}

		int numberOfStandingPersons = 0;
		int totalNumberOfPersonsNeeded = 0;

		for (int sl = 0; sl < maxS+1; sl++)
		{
			int personsNeededForThisLevel = max(0, sl - numberOfStandingPersons);
			totalNumberOfPersonsNeeded += personsNeededForThisLevel;
			numberOfStandingPersons += shynessLevels[sl] + personsNeededForThisLevel;
		}

		cout << "Case #" << t << ": " << totalNumberOfPersonsNeeded << endl;
	}

	return;
}