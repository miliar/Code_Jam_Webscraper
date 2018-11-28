#include <iostream>

using namespace std;

int main()
{
	int n, a, b, ma[4][4], mb[4][4], count, r;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		count = 0;
		cin >> a;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> ma[j][k];
			}
		}
		cin >> b;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> mb[j][k];
			}
		}
		a--; b--;
		int t;
		for (int j = 0; j < 4; j++)
		{
			t = ma[a][j];
			for (int k = 0; k < 4; k++)
			{
				if (mb[b][k] == t)
				{
					count++;
					r = t;
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (count == 1) cout << r << "\n";
		else if (count == 0) cout << "Volunteer cheated!\n";
		else cout << "Bad magician!\n";
	}
	return 0;
}