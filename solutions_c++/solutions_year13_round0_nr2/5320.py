#include <iostream>

using namespace std;

int tablica[200][200];

int main ()
{
	int t, n, m;
	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		bool jest = true;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> tablica[i][j];
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				bool znalazl = false;
				for (int p = 0; p < n; p++)
				{
					if (tablica[i][j] < tablica[p][j])
						break;
					if (p == n - 1)
						znalazl = true;
				}
				for (int p = 0; p < m; p++)
				{
					if (tablica[i][j] < tablica[i][p])
						break;
					if (p == m - 1)
						znalazl = true;
				}
				if (znalazl == false)
					jest = false;
			}
		}
		cout << "Case #" << k; 
		if (jest == true)
			cout << ": YES";
		else
			cout << ": NO";
		cout << endl;
	}
	return 0;
}