#include <iostream>
#include <vector>
#include <string>
using namespace std;

int R, C;
vector<string> rows;
bool impossible;

bool test_dir(int i, int j, char dir)
{
	//cerr << "test_dir: " << i << ", " << j << ", " << dir << ": ";
	int dir_x = (dir == '>') ? 1 : ((dir == '<') ? -1 : 0);
	int dir_y = (dir == 'v') ? 1 : ((dir == '^') ? -1 : 0);
	int x = i + dir_x, y = j + dir_y;
	//cerr << x << ", " << y << ", " << dir_x << ", " << dir_y << " ";
	while ((x >= 0) && (x < C) && (y >= 0) && (y < R))
	{
		if (rows[y][x] != '.')
		{
			//cerr << "true: " << x << ", " << y << endl;
			return true;
		}
		x += dir_x, y += dir_y;
	}
	//cerr << "false" << endl;
	return false;
}

bool test_arrow(int i, int j)
{
	//cerr << "test_arrow: " << i << ", " << j << ", " << rows[j][i] << ": ";
	if (rows[j][i] == '.')
	{
		//cerr << "false0" << endl;
		return false;
	}
	if (test_dir(i, j, rows[j][i]))
	{
		//cerr << "false" << endl;
		return false;
	}

	if (test_dir(i, j, '<') || test_dir(i, j, '>') || test_dir(i, j, '^') || test_dir(i, j, 'v'))
	{
		//cerr << "true" << endl;
		return true;
	}
	//cerr << "impossible" << endl;
	impossible = true;
	return false;
}

int main()
{
	int T;
	cin >> T;
	for (int case_num = 1; case_num <= T; ++case_num)
	{
		cin >> R >> C;
		rows.resize(R);
		for (int j = 0; j < R; ++j)
			cin >> rows[j];

		int num_arrows = 0;
		impossible = false;
		for (int j = 0; j < R; ++j)
			for (int i = 0; i < C; ++i)
				if (test_arrow(i, j))
					++num_arrows;
		cout << "Case #" << case_num << ": ";
		if (impossible)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << num_arrows << endl;
	}
	return 0;
}