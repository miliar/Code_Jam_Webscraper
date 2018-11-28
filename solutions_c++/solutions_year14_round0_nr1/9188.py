#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int row;
		int line[4];
		int found = 0;
		int foundCount = 0;

		cin >> row;
		row--;
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
			{
				int card;
				cin >> card;
				if (r == row)
					line[c] = card;
			}

		cin >> row;
		row--;
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
			{
				int card;
				cin >> card;

				if (r == row)
					for (int i = 0; i < 4; i++)
						if (line[i] == card)
						{
							if (foundCount == 0)
								found = card;
							foundCount++;
						}
			}

		cout << "Case #" << nTestCase << ": ";
		if (foundCount > 1)
			cout << "Bad magician!";
		else if (foundCount == 1)
			cout << found;
		else
			cout << "Volunteer cheated!";
		cout << endl;
	}

	return 0;
}
