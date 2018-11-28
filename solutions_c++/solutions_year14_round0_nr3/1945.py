#include <iostream>
#include "tasks.h"

using namespace std;

bool map[55][55];
int freeSpace;

int r, c, m;

void makeMove(int sx, int sy)
{
	for (int k = -1; k <= 1; ++k)
		for (int l = -1; l <= 1; ++l)
		{
			int x = sx + l;
			int y = sy + k;

			if (x < 0 || x >= c || y < 0 || y >= r)
				continue;

			map[x][y] = true;
		}
}

int calculateMove(int sx, int sy)
{
	int used = 0;

	for (int k = -1; k <= 1; ++k)
		for (int l = -1; l <= 1; ++l)
		{
			int x = sx + l;
			int y = sy + k;

			if (x < 0 || x >= c || y < 0 || y >= r)
				continue;

			if (map[x][y] == true)
				continue;

			++used;
		}

	return used;
}

bool doMagic()
{
	for (int y = 0; y < 55; ++y)
		for (int x = 0; x < 55; ++x)
			map[x][y] = false;

	freeSpace = r * c - m - 1;

	map[0][0] = true;

	bool impossible = false;
	bool found = false;

	while (!impossible && !found)
	{
		bool moved = false;

		int sx = 0;
		int sy = 0;
		int x = 0;
		int y = 0;
		bool state = false;

		while (!moved && x < c && y < r)
		{
			if (map[x][y] == true)
			{
				int used = calculateMove(x, y);

				if (used != 0 && used <= freeSpace)
				{
					moved = true;
					freeSpace -= used;

					makeMove(x, y);
				}
			}

			if (state == false)
			{
				++x;

				if (x == c)
				{
					x = sx;
					state = true;
				}
			}
			else
			{
				++y;

				if (y == r)
				{
					state = false;

					++sx;
					++sy;

					y = sy;
				}
			}
		}
		
		if (!moved)
		{
			impossible = true;
		}
		else if (freeSpace == 0)
		{
			found = true;
		}
	}

	return impossible ? false : true;
}

void minesweeperMaster()
{
	int cases;
	cin >> cases;

	for (int n = 1; n <= cases; ++n)
	{
		cin >> r;
		cin >> c;
		cin >> m;

		bool reversed = false;

		if (r > c)
		{
			int temp = r;
			r = c;
			c = temp;

			reversed = true;
		}

		bool val = doMagic();

		cout << "Case #" << n << ":" << endl;

		if (!val)
			cout << "Impossible" << endl;
		else
		{
			if (reversed)
			{
				for (int y = 0; y < c; ++y)
				{
					for (int x = 0; x < r; ++x)
					{
						if (x == 0 && y == 0)
							cout << "c";
						else if (map[y][x] == true)
							cout << ".";
						else
							cout << "*";
					}

					cout << endl;
				}
			}
			else
			{
				for (int y = 0; y < r; ++y)
				{
					for (int x = 0; x < c; ++x)
					{
						if (x == 0 && y == 0)
							cout << "c";
						else if (map[x][y] == true)
							cout << ".";
						else
							cout << "*";
					}

					cout << endl;
				}
			}
		}
	}

	system("pause");
}