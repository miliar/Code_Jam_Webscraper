#include <iostream>

using namespace std;

int main() {
		int testCases;
		cin >> testCases;
		for (int i = 1; i <= testCases; i++)
		{
			int SMax;
			cin >> SMax;
			int people[SMax];
			char k;
			for (int j = 0; j <= SMax; j++)
			{
				cin >> k;
				people[j] = k - '0';
			}
			int aPersons = 0;
			int persons = people[0];
			for (int j = 1; j <= SMax; j++) {
				if (j > persons)
				{
					aPersons += j - persons;
					persons += j - persons;
				}
				persons += people[j];
			}
			cout << "Case #" << i << ": " << aPersons << endl;
		}
}
