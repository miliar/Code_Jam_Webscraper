/*
ID: tupcuham1
PROG: prime3
LANG: C++11
*/
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>

using namespace std;

typedef long long ll;

ofstream fout("arrows.out");
ifstream fin("arrows.in");

const char STOP = '.';
const char UP = '^';
const char DOWN = 'v';
const char LEFT = '<';
const char RIGHT = '>';

int h, w;
char table[100][100];

int numOuter[100][100];
bool isImpossible()
{
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			numOuter[y][x] = 0;
		}
	}
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			numOuter[y][x] |= 1;
			if (table[y][x] != STOP) break;
		}
		for (int x = w - 1; x >= 0; x--)
		{
			numOuter[y][x] |= 2;
			if (table[y][x] != STOP) break;
		}
	}
	for (int x = 0; x < w; x++)
	{
		for (int y = 0; y < h; y++)
		{
			numOuter[y][x] |= 4;
			if (table[y][x] != STOP) break;
		}
		for (int y = h - 1; y >= 0; y--)
		{
			numOuter[y][x] |= 8;
			if (table[y][x] != STOP) break;
		}
	}

	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			if (numOuter[y][x] == 15 && table[y][x] != STOP) return true;
		}
	}
	return false;
}

int f()
{
	int res = 0;
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			switch (table[y][x])
			{
			case LEFT:
			{
				if (numOuter[y][x] & 1) res++;
			}break;
			case RIGHT:
			{
				if (numOuter[y][x] & 2) res++;
			}break;
			case UP:
			{
				if (numOuter[y][x] & 4) res++;
			}break;
			case DOWN:
			{
				if (numOuter[y][x] & 8) res++;
			}break;
			}
		}
	}
	return res;
}

int main()
{
	int numTests;
	fin >> numTests;
	for (int t = 1; t <= numTests; t++)
	{
		fin >> h >> w;
		for (int y = 0; y < h; y++)
		{
			for (int x = 0; x < w; x++)
			{
				fin >> table[y][x];
			}
		}

		fout << "Case #" << t << ": ";
		if (isImpossible())
		{
			fout << "IMPOSSIBLE";
		}
		else
		{
			fout << f();
		}
		fout << endl;
	}

	return 0;
}

/*
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>

using namespace std;

typedef long long ll;


*/