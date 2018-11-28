#include <iostream>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int ti = 0; ti < t; ++ti)
	{
		cout << "Case #" << (ti + 1) << ": ";
		int a[100][100];
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> a[i][j];
		bool bad = false;
		for (int i = 0; !bad && i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				//if (i == 0 || i == n-1 || j == 0 || j == m-1)
				//	continue;
				
				bool found = false;
				
				// horizontal
				for (int k = 0; k <= m; ++k)
				{
					if (k == m)
						found = true;
					else if (a[i][k] > a[i][j])
						break;
				}

				// vertical 
				for (int k = 0; !found && k <= n; ++k)
				{
					if (k == n)
						found = true;
					else if (a[k][j] > a[i][j])
						break;
				}

				if (!found)
				{
					bad = true;
					break;
				}
			}
		}

		if (bad)
			cout << "NO";
		else 
			cout << "YES";
		cout << endl;

	}
	return 0;
}