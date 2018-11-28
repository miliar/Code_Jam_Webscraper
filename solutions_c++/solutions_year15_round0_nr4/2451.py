#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

bool test1(int r, int c) { return true; }

bool test2(int r, int c) { return (~r | ~c) & 1; } // r or c is even 

bool test3(int r, int c)
{
	if ((r*c) % 3) return false;
	if (r == 1 || c == 1) return false;
	return true;
}

bool test4(int r, int c)
{
	if (r == 4)
		if (c == 4 || c == 3) return true;
	if (c == 4)
		if (r == 4 || r == 3) return true;
	return false;
}

int main()
{
	ifstream file;
	file.open("c.in");
	int t, x, r, c;
	file >> t;
	for (int k = 1; k <= t; k++)
	{
		file >> x >> r >> c;
		bool gabeWins; // can fill board
		switch (x)
		{
		case 1: gabeWins = test1(r, c); break;
		case 2: gabeWins = test2(r, c); break;
		case 3: gabeWins = test3(r, c); break;
		case 4: gabeWins = test4(r, c); break;
		}

		printf("Case #%d: %s\n", k, gabeWins ? "GABRIEL" : "RICHARD");
	}
	file.close();
}
