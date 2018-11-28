#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

void run(istream& inf, ostream &outf)
{
	int x, r, c;
	inf >> x >> r >> c;
	bool possible = true;
	if ((x > r && x > c) || c * r % x != 0)
		possible = false;
	else if (x == 1 || x == 2)
		possible = true;
	else
		possible = !(c - r >= 2 || r - c >= 2);
	outf << (possible ? "GABRIEL" : "RICHARD") << endl;
}

int main()
{
	ifstream inf("D:/Downloads/a-small.in");
	ofstream outf("D:/Downloads/a-small.out");

	int t;
	inf >> t;
	for (int i = 0; i < t; i++)
	{
		outf << "Case #" << (i + 1) << ": ";
		run(inf, outf);
	}

	return 0;
}