#include <fstream>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

void run(istream& inf, ostream &outf)
{
	int max, curr = 0, added = 0;
	inf >> max >> ws;
	for (int i = 0; i <= max; i++)
	{
		int num = inf.get() - '0';
		if (curr < i)
		{
			added += i - curr;
			curr = i;
		}
		curr += num;
	}
	outf << added << endl;
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