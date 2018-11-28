#include <iostream>
#include <string>

using namespace std;


void solve( int testcase, int sMax, string people)
{
	int needPeople = 0;
	int currentPeople = 0;

	for (int level = 0; level <= sMax; level++)
	{
		int audience = people[level] - '0';

		if (audience == 0)
			continue;

		if (level > currentPeople)
		{
			needPeople += level - currentPeople;
			currentPeople += level - currentPeople;
		}

		currentPeople += audience;

	}

	cout << "Case #" << testcase << ": " << needPeople << endl;
	return;
}



int main()
{
	int T = 0;

	cin >> T;

	for(int testcase = 0; testcase < T; testcase++)
	{
		int sMax = 0;
		string people;

		cin >> sMax;
		cin >> people;

		solve(testcase+1, sMax, people);
	}

	return 0;
}
