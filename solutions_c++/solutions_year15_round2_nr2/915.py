#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <functional>

using namespace std;

int solve(int R, int C, int N)
{
	vector<vector<int>> vRooms(R);
	for (int i = 0; i < R; i++)
	{
		vRooms[i] = vector<int>(C);
		for (int j = 0; j < C; j++)
		{
			int value = 4;
			if (C == 1 || R == 1)
				value--;

			if (j == 0 || j == C - 1)
			{
				value--;
			}
			if (i == 0 || i == R - 1)
			{
				value--;
			}
			vRooms[i][j] = value;
		}
	}

	int res = R*(C - 1) + (R - 1)*C;

	int processed = 0;
	while (N < R * C - processed)
	{
		int Max = -1;
		int rMax = -1;
		int cMax = -1;
		bool found = false;
		for (int i = 0; i < R && !found; i++)
		{
			for (int j = 0; j < C && !found; j++)
			{
				if (vRooms[i][j] == -1)
					continue;
				if (vRooms[i][j] == 4)
				{
					res -= vRooms[i][j];
					vRooms[i][j] = -1;
					vRooms[i - 1][j] -= 1;
					vRooms[i + 1][j] -= 1;
					vRooms[i][j - 1] -= 1;
					vRooms[i][j + 1] -= 1;
					processed++;
					found = true;
					
					break;
				}
				else
				{
					if (vRooms[i][j] > Max)
					{
						Max = vRooms[i][j];
						rMax = i;
						cMax = j;
					}
				}
			}
		}
		if (!found)
		{
			res -= vRooms[rMax][cMax];
			vRooms[rMax][cMax] = -1;
			if (rMax > 0)
				vRooms[rMax - 1][cMax] -= 1;
			if (cMax > 0)
				vRooms[rMax][cMax - 1] -= 1;
			if (rMax < R - 1)
				vRooms[rMax + 1][cMax] -= 1;
			if (cMax < C - 1)
				vRooms[rMax][cMax + 1] -= 1;

			processed++;
		}
	}

	return res;
}

int main()
{
	//ifstream in("B-small-attempt0_.in");
	//ofstream out("B-small-attempt0____.out");

	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int iTasks;
	in >> iTasks;

	for (int iCount = 1; iCount <= iTasks; iCount++)
	{
		int R, C, N;
		in >> R >> C >> N;
		int odd = (R * C) % 2;
		int result = 0;
		if (N > (R*C) / 2 + odd)
		{
			if (odd > 0)
			{
				if (R > 1 && C > 1 && N == (R*C) / 2 + odd + 1)
					result = 3;
			}
			if (result == 0)
				result = solve(R, C, N);
		}

		out << "Case #" << iCount << ": " << result << endl;
	}
	return 0;
}
