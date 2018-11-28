#include <iostream>
using namespace std;

int t;
int a1;
int tab1[10][10];
int tab2[10][10];
int a2;

bool spr[10];

int main ()
{
	ios_base::sync_with_stdio (0);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> a1;
		for (int x = 1; x <= 4; x++)
		{
			for (int y = 1; y <= 4; y++)
			{
				cin >> tab1[x][y];
			}
		}
		cin >> a2;
		for (int x = 1; x <= 4; x++)
		{
			for (int y = 1; y <= 4; y++)
			{
				cin >> tab2[x][y];
			}
		}
		for (int x = 1; x <= 4; x++) spr[x] = false;
		for (int x = 1; x <= 4; x++)
		{
			for (int y = 1; y <= 4; y++)
			{
				if (tab1[a1][x] == tab2[a2][y]) spr[y] = true;
			}
		}
		int il = 0;
		int l = 0;
		for (int x = 1; x <= 4; x++)
		{
			if (spr[x] == true)
			{
				il++;
				l = tab2[a2][x];
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (il == 0) cout << "Volunteer cheated!\n";
		if (il == 1) cout << l << "\n";
		if (il > 1) cout << "Bad magician!\n";
	}
	return 0;
}
