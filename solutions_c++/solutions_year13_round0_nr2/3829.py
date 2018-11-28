#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	ifstream cin ( "input.txt" );
	ofstream cout ( "output.txt" );
	int t;
	cin >> t;
	int all = t;
	while (t--)
	{
		bool flag = false;
		cout << "Case #" << all-t << ": ";
		int n, m;
		cin >> n >> m;
		vector < vector <int> > a (n, vector <int> (m));
		vector <int> rows (n, -1);
		vector <int> columns (m, -1);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> a [i][j];
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				rows [i] = max (rows [i], a [i][j]);
		for (int j = 0; j < m; ++j)
			for (int i = 0; i < n; ++i)
				columns [j] = max (columns [j], a [i][j]);
		for (int i = 0; (i < n) && (!flag); ++i)
			for (int j = 0; (j < m) && (!flag); ++j)
				if (a [i][j] != min (rows [i], columns [j]))
				{
					cout << "NO" << endl;
					flag = true;
				}
		if (!flag)
			cout << "YES" << endl;
	}
}