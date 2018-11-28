#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <string>
using namespace std;

int x, r, c;

bool solve()
{
	cin >> x >> r >> c;
	if (r > c) swap(r,c);

	if (x == 1)
		return true;
	if (x == 2)
	{
		if ((r *c) & 1)
			return false;
		return true;
	}
	if (x == 3)
	{
		if (r == 1)
		{
			return false;
		}
		if (r == 2)
		{
			if (c == 3) 
				return true;
			return false;
		}
		if (r == 3)
		{
			return true;
		}
		if (r == 4)
		{
			return false;
		}
	}
	if (x == 4)
	{
		/*
		#### ##  #   ##  #
		      ## ### ## ###

		*/
		if (r == 1)
		{
			return false;
		}
		if (r == 2)
		{
			return false;
		}
		if (r == 3)
		{
			if (c == 4)
				return true;
			return false;
		}
		if (r == 4)
		{
			return true;
		}
	}
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		printf("Case #%d: ", test);
		printf(solve()?"GABRIEL":"RICHARD");
		printf("\n");
	}
}