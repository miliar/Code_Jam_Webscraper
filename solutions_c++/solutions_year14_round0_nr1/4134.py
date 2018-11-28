#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
	int k;
	int caso = 1;
	cin >> k;
	while (k--)
	{
		int bucket[17];
		for (int i = 0; i < 17; i++) bucket[i] = 0;
		int temp;
		int row;
		int times = 2;
		while (times--)
		{
			cin >> row;
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					cin >> temp;
					if (row - 1 == i)
					{
						bucket[temp]++;
					}
				}
			}
		}

		int moreThanOne = 0;
		int lastMoreThanOne;
		
		for (int i = 1; i < 17; i++)
		{
			if (bucket[i] == 2)
			{
				moreThanOne++;
				lastMoreThanOne = i;
			}
		}

		cout << "Case #" << caso++ << ": ";

		if (moreThanOne == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if (moreThanOne == 1)
		{
			cout << lastMoreThanOne << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}