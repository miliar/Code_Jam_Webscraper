#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
char mul(char x, char y)
{
	if (x == '1')
		return y;
	else if (x == 'i')
	{
		if (y == '1')
			return 'i';
		if (y == 'i')
			return '1';
		if (y == 'j')
			return 'k';
		if (y == 'k')
			return 'j';
	}
	else if (x == 'j')
	{
		if (y == '1')
			return 'j';
		if (y == 'i')
			return 'k';
		if (y == 'j')
			return '1';
		if (y == 'k')
			return 'i';
	}
	else if (x == 'k')
	{
		if (y == '1')
			return 'k';
		if (y == 'i')
			return 'j';
		if (y == 'j')
			return 'i';
		if (y == 'k')
			return '1';
	}
}

int op(char x, char y)
{
	if (x == y || (x == 'i' && y == 'k') || (x == 'j' && y == 'i') || (x == 'k' && y == 'j'))
		return -1;
	return 1;
}

int main()
{
	ifstream inf("in.txt");
	int t, T;
	inf >> T;
	map<char, map<char, char> > m;
	ofstream outf("res.txt");
	for (t = 1;t <= T;t++)
	{
		int x, r, c;
		inf >> x >> r >> c;
		if (x == 1 ||
			(x == 2 && (r * c) % 2 == 0) ||
			(x == 3 && ((r == 2 && c == 3) || (r == 3 && c == 2) || (r == 3 && c == 3)|| (r == 4 && c == 3) || (r == 3 && c == 4))) ||
			(x == 4 && ((r == 3 && c == 4) || (r == 4 && c == 3) || (r == 4 && c == 4)))
			)

			outf << "Case #" << t << ": " << "GABRIEL" << endl;
		else
			outf << "Case #" << t << ": " << "RICHARD" << endl;
	}
    return 0;
}