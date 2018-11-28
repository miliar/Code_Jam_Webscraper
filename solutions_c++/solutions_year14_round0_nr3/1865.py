#if 1

#include <iostream>
#include <vector>

using namespace std;

int dr[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
int dc[] = { -1, -1, -1, 0, 0, 1, 1, 1 };

int dr2[] = { -1, 1, -1, 1 };
int dc2[] = { -1, -1, 1, 1 };

bool inbounds(int R, int C, int i, int j)
{
	return (i >= 0 && j >= 0 && i < R && j < C);
}

bool recurse(vector<vector<char>> board, int R, int C, int emptysleft)
{
	if (emptysleft < 0) return false;
	if (emptysleft == 0)
	{
		for (int i = 0; i < R; ++i)
		{
			for (int j = 0; j < C; ++j)
			{
				char c = board[i][j];
				cout << (c == '0' ? '.' : c);
			}
			cout << endl;
		}
		return true;
	}
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			if (board[i][j] == '.')
			{
				/*bool search0 = false;
				for (int k = 0; !search0 && k < 4; ++k)
				{
					if (inbounds(R, C, i + dr2[k], j + dc2[k]) && (board[i + dr2[k]][j + dc2[k]] == '0' || board[i + dr2[k]][j + dc2[k]] == 'c')) search0 = true;
				}
				if (!search0) continue;*/
				board[i][j] = '0';
				int spacesneeded = 0;
				auto cpy = board;
				for (int k = 0; k < 8; ++k)
				{
					if (inbounds(R, C, i + dr[k], j + dc[k]) && board[i + dr[k]][j + dc[k]] == '*')
					{
						spacesneeded += 1;
						cpy[i + dr[k]][j + dc[k]] = '.';
					}
				}
				if (recurse(cpy, R, C, emptysleft - spacesneeded)) return true;
			}
		}
	}
	return false;
}

void trygeneralboard(int R, int C, int M)
{
	vector<vector<char>> vec(R, vector<char>(C, '*'));
	if (M + 1 == R*C)
	{
		vec[0][0] = 'c';
		recurse(vec, R, C, 0);
	}
	else
	{
		int spaceused = 1;
		vec[0][0] = 'c';
		if (R > 1)
		{
			vec[1][0] = '.';
			spaceused++;
		}
		if (C > 1)
		{
			vec[0][1] = '.';
			spaceused++;
		}
		if (C > 1 && R > 1)
		{
			vec[1][1] = '.';
			spaceused++;
		}

		if (!recurse(vec, R, C, R*C - M - spaceused))
		{
			cout << "Impossible" << endl;
		}
	}
}

void doit(int casenum)
{
	cout << "Case #" << casenum << ":" << endl;

	int R, C, M;
	cin >> R >> C >> M;

	/*if (R == 1)
	{
		cout << 'c';
		spaceleft -= 1;
		for (int i = 1; i < C; ++i)
		{
			if (spaceleft)
			{
				cout << '.';
				spaceleft -= 1;
			}
			else
			{
				cout << '*';
			}
		}
		cout << endl;
	}
	else if (C == 1)
	{
		cout << 'c' << endl;
		spaceleft -= 1;
		for (int i = 1; i < R; ++i)
		{
			if (spaceleft)
			{
				cout << '.' << endl;
				spaceleft -= 1;
			}
			else
			{
				cout << '*' << endl;
			}
		}
	}
	else*/
	{
		trygeneralboard(R, C, M);
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) doit(i);
	return 0;
}

#endif