/* Author: Tran Hua Duc/Dave */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	unsigned i, j, t;

	string s;
	string lastWord[100];

	//read input
	fstream ifile;
	ifile.open("A-large.in", ios::in);
	ifile >> t;

	for (i = 0; i < t; i++)
	{
		ifile >> s;

		//calculate result
		lastWord[i] = s[0];
		for (j = 1; j < s.length(); j++)
		{
			if (lastWord[i][0] > s[j])
				lastWord[i] = lastWord[i] + s[j];
			else
				lastWord[i] = s[j] + lastWord[i];
		}
	}

	ifile.close();

	//output result
	ofstream ofile;
	ofile.open("output-l.txt", ios::out);

	for (i = 0; i < t; i++)
		ofile << "Case #" << i + 1 << ": " << lastWord[i] << endl;

	return 0;
}