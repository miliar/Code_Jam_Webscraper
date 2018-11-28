//Source by Kasimir Tanner, Task: Standing Ovation, C++
#include <iostream>

using namespace std;

int main()
{
	int testCases;
	cin >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		int maxShynessLevel;
		cin >> maxShynessLevel;
		maxShynessLevel++;
		int friendsNeeded = 0;
		int totalStanding = 0;
		for (int j = 0; j < maxShynessLevel; j++)
		{
			char p;
			cin >> p;
			int people = static_cast<int>(p) - 48;

			if(totalStanding < j)
			{
				int friends = j - totalStanding;
				friendsNeeded += friends;
				totalStanding += friends;
			}
			totalStanding += people;
		}
		cout << "Case #" << i+1 << ": " << friendsNeeded << endl;
	}
}
