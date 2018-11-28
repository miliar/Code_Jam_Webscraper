#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int ncases;
	cin >> ncases;
	for (int i = 1; i <= ncases; i++)
	{
		int r1, r2;
		vector<int> first, second;
		cin >> r1;

		for (int r = 1; r <= 4; r++)
		{
			int temp;
			for (int c = 0; c < 4; c++)
			{
				cin >> temp;
				if (r == r1)
					first.push_back(temp);
			}
		}

		cin >> r2;
		for (int r = 1; r <= 4; r++)
		{
			int temp;
			for (int c = 0; c < 4; c++)
			{
				cin >> temp;
				if (r == r2)
					second.push_back(temp);
			}
		}

		int found = 0;
		int lastfound = -1;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (first[j] == second[k])
				{
					found++;
					lastfound = second[k];
				}
			}
		}

		cout << "Case #" << i << ": ";
		if (found == 1)
			cout << lastfound << "\n";
		else if (found == 0)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
	return 0;
}