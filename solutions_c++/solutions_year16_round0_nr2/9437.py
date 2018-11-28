/* Author: Tran Hua Duc/Dave */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int pFlip(string pancake, int flips, int depth)
{
	//exit if on uppermost pancake
	if (depth == -1)
		return flips;

	//flip if (currentface * (-1^flips) == -currectface)
	if (pancake[depth] == '+' && flips % 2 == 0)
		return pFlip(pancake, flips, depth - 1);
	else if (pancake[depth] == '-' && flips % 2 == 1)
		return pFlip(pancake, flips, depth - 1);
	else
	{
		return pFlip(pancake, flips + 1, depth - 1);
	}
}

int main(int argc, char** argv)
{
	int i, t, tres[100];
	string pancakes[100];

	fstream ifile;
	ifile.open("B-large.in", ios::in);
	ifile >> t;

	for (i = 0; i < t; i++)
	{
		ifile >> pancakes[i];
		tres[i] = pFlip(pancakes[i], 0, pancakes[i].length() - 1);
	}

	ifile.close();

	ofstream ofile;
	ofile.open("output_l.txt", ios::out);

/*	for (i = 0; i < t; i++)
		ofile << pancakes[i] << endl;	*/

	for (i = 0; i < t; i++)
		ofile << "Case #" << i + 1 << ": " << tres[i] << endl;

	return 0;
}