
#include <cstring>
#include <cassert>
#include <cstdio>
#include <vector>
#include <set>
#include <iostream>

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))

void generateInput ()
{
	printf ("64\n");
	for (int i = 1; i <= 4; ++i)
		for (int j = 1; j <= 4; ++j)
			for (int k = 1; k <= 4; ++k)
					printf ("%d %d %d\n", i, j, k);
}

std::string getWinner (int x, int r, int c)
{
	std::string first("RICHARD");
	std::string second("GABRIEL");
	if (x == 1)
	{
		return second;
	}
	if ((r*c)%x != 0)
	{
		return first;
	}

	if (x == 2)
	{
		if ((r*c)%2 == 0)
			return second;
		else
			return first;
	}

	if (x == 3)
	{
		if ((min(c, r)==2 && max(c, r)==3) ||
			(min(c, r)==3 && max(c, r)==4) ||
			(min(c, r)==	3 && max(c, r)==3))
		{
			return second;
		} else {
			return first;
		}
	}

	if (x == 4)
	{
		if ((r == 4 && c == 4) ||
			(min(c, r)==3 && max(c, r)==4))
		{
			return second;
		} else {
			return first;
		}
	}

	return std::string();
}

void ominous_omino ()
{
	int tcNum;
	std::cin >> tcNum;

	// printf ("Num of TCs = %d\n", tcNum);

	for (int tc = 0; tc < tcNum; ++tc)
	{
		int x, r, c;
		std::cin >> x;
		std::cin >> r;
		std::cin >> c;

		printf ("Case #%d: %s\n", tc+1, getWinner(x, r, c).c_str());

	}
}


