#include <iostream>
using namespace std;

int main()
{
	int t;
	int n, m;
	int h[100][100];
	int s[100][100];
	int maxrow[100];
	int maxcol[100];
	bool y;

	cin >> t;

	for(int i = 0; i < t; i++)
	{
		y = true;

		cin >> n >> m;

		for(int j = 0; j < n; j++)
		{
			for(int k = 0; k < m; k++)
			{
				s[j][k] = 100;
				maxcol[k] = 0;
			}

			maxrow[j] = 0;
		}

		for(int j = 0; j < n; j++)
		{
			for(int k = 0; k < m; k++)
			{
				cin >> h[j][k];

				if(h[j][k] > maxcol[k])
					maxcol[k] = h[j][k];

				if(h[j][k] > maxrow[j])
					maxrow[j] = h[j][k];
			}
		}

		for(int j = 0; j < n; j++)
		{
			for(int k = 0; k < m; k++)
			{
				s[j][k] = maxrow[j];
			}
		}

		for(int j = 0; j < m; j++)
		{
			for(int k = 0; k < n; k++)
			{
				if(s[k][j] > h[k][j])
					s[k][j] = maxcol[j];
			}
		}

		for(int j = 0; j < n; j++)
		{
			for(int k = 0; k < m; k++)
			{
				if(s[j][k] != h[j][k])
				{
					y = false;
					break;
				}
			}
		}

		cout << "Case #" << i + 1 << ": ";

		if(y == true)
			cout << "YES";
		else
			cout << "NO";

		cout << endl;
	}

	return 0;
}