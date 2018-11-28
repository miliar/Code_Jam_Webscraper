#include <iostream>

using namespace std;

int main()
{
	int nbCases = 0;
	int audience[1001] = { 0 };
	cin >> nbCases;
	for (int i = 0; i < nbCases; i ++)
	{
		int size;
		cin >> size;
		char c;
		for (int j = 0; j < size + 1; j++)
		{
			cin >> c;
			audience[j] = (int)(c - '0');
		}
		int currentFriends = 0;
		int currentStand = 0;
		for (int j = 0; j < size + 1; j ++)
		{
			if (currentStand < j)
			{
				int var = j - currentStand;
				currentFriends += var;
				currentStand += var;
			}
			currentStand += audience[j];
		}
		cout << "Case #" << i + 1 << ": " << currentFriends << endl;
	}
}
