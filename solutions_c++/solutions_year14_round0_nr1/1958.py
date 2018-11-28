#include <iostream>
#include <set>

using namespace std;

int main()
{
	int nrOfCases;
	cin >> nrOfCases;
	for (int c = 1; c <= nrOfCases; c++)
	{
		int g1, g2;
		cin >> g1;
		int field1[4][4];
		
		
		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				cin >> field1[y][x];
			}
		}
		
		cin >> g2;
		
		int field2[4][4];
		
		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				cin >> field2[y][x];
			}
		}
		
		bool oneMatch = false;
		bool twoMatches = false;
		int match = -1;
		for (int a = 0; a < 4; a++)
		{
			for (int b = 0; b < 4; b++)
			{
				if (field1[g1 - 1][a] == field2[g2 - 1][b])
				{
					if (oneMatch) twoMatches = true;
					else 
					{
						oneMatch = true;
						match = field1[g1 - 1][a];
					}
				}
			}
		}
		
		cout << "Case #" << c << ": ";
		
		if (oneMatch && !twoMatches) cout << match << endl;
		else if (twoMatches) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
		
	}
}
