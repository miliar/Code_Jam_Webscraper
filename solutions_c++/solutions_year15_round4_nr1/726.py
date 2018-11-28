#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

char m[105][105];
int r, c;

bool checkUp(int i, int j)
{
	i--;
	while (i >= 0)
		if (m[i][j] != '.')
			return true;
		else
			i--;
	return false;
}

bool checkDown(int i, int j)
{
	i++;
	while (i < r)
		if (m[i][j] != '.')
			return true;
		else
			i++;
	return false;
}

bool checkLeft(int i, int j)
{
	j--;
	while (j >= 0)
		if (m[i][j] != '.')
			return true;
		else
			j--;
	return false;
}

bool checkRight(int i, int j)
{
	j++;
	while (j < c)
		if (m[i][j] != '.')
			return true;
		else
			j++;
	return false;
}

int main()
{
	int tt;
	
	cin >> tt;
	
	for (int t = 1; t <= tt; ++t)
	{
		cout << "Case #" << t << ": ";
		
		cin >> r >> c;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				cin >> m[i][j];
		
		int cnt = 0;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if (m[i][j] == '.')
					continue;
				bool up = checkUp(i, j);
				bool down = checkDown(i, j);
				bool left = checkLeft(i, j);
				bool right = checkRight(i, j);
				if (!up && !down && !left && !right)
				{
					cnt = -1;
					break;
				}
				if ((m[i][j] == '^') && !up)
					cnt++;
				if ((m[i][j] == 'v') && !down)
					cnt++;
				if ((m[i][j] == '<') && !left)
					cnt++;
				if ((m[i][j] == '>') && !right)
					cnt++;
			}
			if (cnt == -1)
				break;
		}
		
		if (cnt == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << cnt << endl;
	}

	return 0;
}
