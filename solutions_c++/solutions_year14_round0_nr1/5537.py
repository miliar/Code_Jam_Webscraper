#include <iostream>
#include "tasks.h"

using namespace std;

void magicTrick()
{
	int cases;
	cin >> cases;

	for (int n = 1; n <= cases; ++n)
	{
		int tab1[4][4];
		int tab2[4][4];

		int answer1;
		int answer2;

		cin >> answer1;
		--answer1;

		for (int y = 0; y < 4; ++y)
			for (int x = 0; x < 4; ++x)
			{
				int v;
				cin >> v;

				tab1[y][x] = v;
			}

		cin >> answer2;
		--answer2;

		for (int y = 0; y < 4; ++y)
		{
			for (int x = 0; x < 4; ++x)
			{
				int v;
				cin >> v;

				tab2[y][x] = v;
			}
		}
		
		bool cheated = true;
		int card = -1;
		bool badMagic = false;

		for (int y = 0; y < 4; ++y)
		{
			for (int x = 0; x < 4; ++x)
			{
				if (tab1[answer1][y] == tab2[answer2][x])
				{
					if (!cheated)
						badMagic = true;

					cheated = false;

					card = tab1[answer1][y];
				}
			}
		}

		if (cheated)
			cout << "Case #" << n << ": Volunteer cheated!" << endl;
		else if (badMagic)
			cout << "Case #" << n << ": Bad magician!" << endl;
		else
			cout << "Case #" << n << ": " << card << endl;
	}

	system("pause");
}