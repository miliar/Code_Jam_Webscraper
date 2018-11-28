#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int r, c;

bool CheckDirection(const vector<string> &map, int i, int j, int di, int dj)
{
	i += di, j += dj;
	while (i >= 0 && j >= 0 && i < r && j < c)
	{
		if (map[i][j] != '.')
			return true;
		i += di, j += dj;
	}
	return false;
}

int main()
{
	ios_base::sync_with_stdio(false);

	int case_count;
	cin >> case_count;
	for (int case_no = 1; case_no <= case_count; ++case_no)
	{
		cout << "Case #" << case_no << ": ";
		cin >> r >> c;
		vector<string> map(r);
		for (int i = 0; i < r; ++i)
			cin >> map[i];

		bool possible = true;
		int change = 0;

		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if (map[i][j] != '.')
				{
					bool up = CheckDirection(map, i, j, -1, 0);
					bool down = CheckDirection(map, i, j, 1, 0);
					bool left = CheckDirection(map, i, j, 0, -1);
					bool right = CheckDirection(map, i, j, 0, 1);

					if (!up && !down && !left && !right)
					{
						possible = false;
						break;
					}

					switch (map[i][j])
					{
					case '^':
						change += !up;
						break;
					case 'v':
						change += !down;
						break;
					case '<':
						change += !left;
						break;
					case '>':
						change += !right;
						break;
					}
				}
			}
			if (!possible)
				break;
		}

		if (possible)
			cout << change << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}