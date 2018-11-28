#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int N, c1, c2, m, l, j, k, i;
	int iGrid[16], rGrid[16];
	int found;

	cin >> N;
	for (i = 1; i <= N; i++)
	{
		found = -1;
		cin >> c1;
		for (j = 0; j < 16; j++)
		{
			cin >> iGrid[j];
		}
		cin >> c2;
		for (k = 0; k < 16; k++)
		{
			cin >> rGrid[k];
		}

		for (m = 4 * (c1 - 1), l = c1 * 4; m < l; m++)
		{
			for (j = 4 * (c2 - 1), k = c2 * 4; j < k; j++)
			{
				if (iGrid[m] == rGrid[j])
				{
					if (found == -1)
						found = iGrid[m];
					else
					{
						found = -2;
						break;
					}
				}
			}
			if (found == -2)
				break;
		}

		cout << "Case #" << i << ": ";
		if (found == -1)
			cout << "Volunteer cheated!" << endl;
		else if (found == -2)
			cout << "Bad magician!" << endl;
		else
			cout << found << endl;
	}
}
