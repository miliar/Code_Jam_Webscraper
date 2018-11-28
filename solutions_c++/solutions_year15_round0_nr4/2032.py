//Code Jam 2015 Qualifier
//Ominous Omino

#include <iostream>
#include <fstream>
#include <string>


using namespace std;

int main(void)
{
	int t, x, r, c;
	string winner;
	ifstream fin;
	ofstream fout;

	fin.open("D-small-attempt0.in");
	fout.open("output.txt");

	fin >> t;

	for (int i = 1; i <= t; i++)
	{
		fin >> x >> r >> c;

		if ((r*c >= x) && ((r*c) % x == 0) && (r >= (x - 1)) && (c >= (x - 1)) && ((r >= x) || (c >= x)))
			winner = "GABRIEL";
		else winner = "RICHARD";

		fout << "Case #" << i << ": " << winner << endl;		
	}

	return 0;
}