#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifile("pro4s.in");
	ofstream ofile("result4s.out");
	int cases=0, x = 0, r = 0, c = 0;

	ifile >> cases;

	for (int i = 0; i < cases; i++)
	{
		ifile >> x;
		ifile >> r;
		ifile >> c;
		
		if ((r*c % x != 0))
			ofile << "Case #" << i + 1 << ": " << "RICHARD" << '\n';
		else if (((r >= x) && (c >= (x - 1))) || ((c >= x) && (r >= (x - 1))))
			ofile << "Case #" << i + 1 << ": " << "GABRIEL" << '\n';
		else
			ofile << "Case #" << i + 1 << ": " << "RICHARD" << '\n';
	}

	return 0;
}