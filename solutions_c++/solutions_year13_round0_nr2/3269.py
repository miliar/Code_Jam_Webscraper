#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector <vector <int>> lawn;

bool mayDeleteLine(int line)
{
	for (int i = 0; i < lawn[line].size(); i++)
		if (lawn[line][i] != lawn[line][0])
			return false;
	return true;
}

bool mayDeleteColumn(int col)
{
	for (int i = 0; i < lawn.size(); i++)
		if (lawn[i][col] != lawn[0][col])
			return false;
	return true;
}

void deleteColumn(int col)
{
	for (int i = 0; i < lawn.size(); i++)
		lawn[i].erase(lawn[i].begin() + col);
}

void main()
{
	ifstream in("B-large.in");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (int k = 0; k < T; k++)
	{
		int m, n;
		in >> n >> m;

		lawn.clear();
		lawn.reserve(n);
		for (int i = 0; i < n; i++)
		{
			lawn.push_back(vector <int>());
			lawn[i].reserve(m);
		}

		int a;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				in >> a;
				lawn[i].push_back(a);
			}

		if (n == 1 || m == 1)
		{
			out << "Case #" << k + 1 << ": YES" << endl; 
			continue;
		}

		bool isDeleted;
		for (int g = 1; g <= 100; g++)
		{
			isDeleted = false;

			if (n == 0 || m == 0)
				break;

			for (int i = 0; i < n; i++)
				if (lawn[i][0] == lawn[i][m - 1] && lawn[i][0] == g)
					if (mayDeleteLine(i))
					{
						lawn.erase(lawn.begin() + i);
						n--;
						g--;
						isDeleted = true;
						break;
					}

			if (isDeleted)
				continue;

			for (int j = 0; j < m; j++)
				if (lawn[0][j] == lawn[n - 1][j] && lawn[0][j] == g)
					if (mayDeleteColumn(j))
					{
						deleteColumn(j);
						m--;
						g--;
						isDeleted = true;
						break;
					}

			if (isDeleted)
				continue;
		}

		if (m == 0 || n == 0)
			out << "Case #" << k + 1 << ": YES" << endl;
		else
			out << "Case #" << k + 1 << ": NO" << endl;
	}
}
