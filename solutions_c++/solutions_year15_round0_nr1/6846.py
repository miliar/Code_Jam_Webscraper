#include <iostream>
#include <sstream>
using namespace std;

int main(void)
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int sMax;
		cin >> sMax;

		int numOvators = 0;
		int addedMembers = 0;
		for (int s = 0; s <= sMax; s++)
		{
			char c;
			cin >> c;
			stringstream stream;
			stream << c;

			int sCount;
			stream >> sCount;

			int ovatorsNeeded = s - numOvators;
			if (ovatorsNeeded > 0)
			{
				addedMembers += ovatorsNeeded;
				numOvators += ovatorsNeeded;
			}

			numOvators += sCount;
		}

		cout << "Case #" << t << ": " << addedMembers << endl;
	}
}