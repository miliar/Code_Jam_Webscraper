#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int first, second;
		cin >> first;
		int tab[4][4];
		vector<int>poss;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> tab[j][k];
				if (j == first - 1)
					poss.push_back(tab[j][k]);
			}
		}
		cin >> second;
		int res = -1;
		bool many = false;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> tab[j][k];
				if (j == second - 1)
				{
					for (int l = 0; l < 4; l++)
					if (tab[j][k] == poss[l])
					{
						if (res == -1)
							res = poss[l];
						else
							many = true;
					}
				}
			}
		}
		cout << "Case #" << i << ": ";
		if (many)
		{
			cout << "Bad magician!\n";
		}
		else if (res != -1)
		{
			cout << res << endl;
		}
		else
			cout << "Volunteer cheated!\n";
	}
	return 0;
}