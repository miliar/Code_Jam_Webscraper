#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main() {
	// test number is between 1 and 100
	int numberOfTests, maxShyLevel;
	cin >> numberOfTests;
	long long standingAudience = 0;
	long long friendsToInvite = 0;
	std::string strAudience;
	for (int testNumber = 0; testNumber < numberOfTests; ++testNumber) {
		// for small data set: 0 <= maxShyLevel <= 6
		// for large data set: 0 <= maxShyLevel <= 1000
		cin >> maxShyLevel;

		// There will always be at least one person in the audience
		// NOTE: the string will never end with a 0
		cin >> strAudience;

		standingAudience = 0;
		friendsToInvite = 0;
		for (int shyLevel = 0; shyLevel < strAudience.length(); ++shyLevel) {
			int numOfShyPeople = strAudience.at(shyLevel) - '0';
			// I need to show that for this index of shy people to stand up, there must already be 'this index' number of people already standing
			// if my shyLevel is greater than the number of people already standing
			if (shyLevel > standingAudience) {
				// find number of friends to invite
				friendsToInvite += shyLevel - standingAudience;
				standingAudience += shyLevel - standingAudience;
			}
			standingAudience += numOfShyPeople;
		}
		cout << "Case #" << testNumber + 1 << ": " << friendsToInvite << endl;
	}
	return 0;
}