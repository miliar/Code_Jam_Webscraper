#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main () 
{
	int numberOfCases = 0;

	scanf("%d", &numberOfCases);

	for (int caseIndex = 0; caseIndex < numberOfCases; caseIndex++) 
	{
		int maxShy = 0;
		scanf("%d", &maxShy);

		int numberOfStandingPeople = 0;
		int peopleToAddToAudience = 0;

		string audience = "";

		cin >> audience;
		
		for (int S_i = 0; S_i < audience.length(); S_i++) 
		{
		
			int PeopleWithShySi = (int) (audience.at(S_i)) - (int)('0');
			
			if (numberOfStandingPeople < S_i) 
			{
				peopleToAddToAudience += S_i - numberOfStandingPeople;
				numberOfStandingPeople += (S_i - numberOfStandingPeople);
			}

			numberOfStandingPeople += PeopleWithShySi;
		}

		cout << "Case #" << (caseIndex + 1) << ": " << peopleToAddToAudience;

		if (caseIndex != numberOfCases - 1)
			cout << "\r\n";

		cout << std::flush;
	}
}