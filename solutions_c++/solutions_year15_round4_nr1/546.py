#include<iostream>
using namespace std;

char gr[110][110];
bool hasUp[110][110], hasDown[110][110], hasLeft[110][110], hasRight[110][110];

int r, c;

bool valid(int x, int y)
{
	return 0 <= x && x < r && 0 <= y && y < c;
}

int main()
{
	int t, kase = 0;
	cin >> t;
	while (t--)
	{
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			cin >> gr[i];

		for (int i = 0; i < c; i++)
			hasUp[0][i] = false;
		for (int i = 1; i < r; i++)
			for (int j = 0; j < c; j++)
				hasUp[i][j] = hasUp[i - 1][j] | gr[i - 1][j] != '.';
		
		for (int i = 0; i < c; i++)
			hasDown[r - 1][i] = false;
		for (int i = r - 2; i >= 0; i--)
			for (int j = 0; j < c; j++)
				hasDown[i][j] = hasDown[i + 1][j] | gr[i + 1][j] != '.';

		for (int i = 0; i < r; i++)
			hasLeft[i][0] = false;
		for (int i = 0; i < r; i++)
			for (int j = 1; j < c; j++)
				hasLeft[i][j] = hasLeft[i][j - 1] | gr[i][j - 1] != '.';

		for (int i = 0; i < r; i++)
			hasRight[i][c - 1] = false;
		for (int i = 0; i < r; i++)
			for (int j = c - 2; j >= 0; j--)
				hasRight[i][j] = hasRight[i][j + 1] | gr[i][j + 1] != '.';

		bool impossible = false;
		int cnt = 0;
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (gr[i][j] == '^' && !hasUp[i][j])
				{
					if (!hasDown[i][j] && !hasLeft[i][j] && !hasRight[i][j]) impossible = true;
					if (impossible) goto end;
					cnt++;
				}

				if (gr[i][j] == 'v' && !hasDown[i][j])
				{
					if (!hasUp[i][j] && !hasLeft[i][j] && !hasRight[i][j]) impossible = true;
					if (impossible) goto end;
					cnt++;
				}

				if (gr[i][j] == '<' && !hasLeft[i][j])
				{
					if (!hasUp[i][j] && !hasDown[i][j] && !hasRight[i][j]) impossible = true;
					if (impossible) goto end;
					cnt++;
				}

				if (gr[i][j] == '>' && !hasRight[i][j])
				{
					if (!hasUp[i][j] && !hasDown[i][j] && !hasLeft[i][j]) impossible = true;
					if (impossible) goto end;
					cnt++;
				}
			}
		}
	end:
		cout << "Case #" << ++kase << ": ";

		if (impossible)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << cnt << endl;
	}
	return 0;
}