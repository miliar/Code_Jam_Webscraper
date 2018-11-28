#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int h, w;
		int map[100][100];
		cin >> h >> w;

		int rowLevels[100];
		int colLevels[100];
		for (int y = 0; y < h; ++y)
			rowLevels[y] = 0;
		for (int x = 0; x < w; ++x)
			colLevels[x] = 0;

		for (int y = 0; y < h; ++y)
		{
			for (int x = 0; x < w; ++x)
			{
				int a;
				cin >> a;
				map[y][x] = a;
				rowLevels[y] = max(rowLevels[y], a);
				colLevels[x] = max(colLevels[x], a);
			}
		}
		const char* ret = "YES";
		for (int y = 0; y < h; ++y)
		{
			for (int x = 0; x < w; ++x)
			{
				if (map[y][x] < rowLevels[y] && map[y][x] < colLevels[x])
				{
					ret = "NO";
					goto finished_case;
				}
			}
		}
	finished_case:
		cout << "Case #" << (t+1) << ": " << ret << endl;
	}
	return 0;
}
