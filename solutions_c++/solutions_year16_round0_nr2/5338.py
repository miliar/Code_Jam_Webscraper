#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int cases, curCase, flips, k;
	string stack;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");

	fin>>cases;
	curCase = 1;

	while (curCase <= cases)
	{
		flips = 0;
		fin>>stack;

		if (stack[stack.length() - 1] == '-')
			flips = 1;

		for (k = stack.length() - 2; k >= 0; k--)
		{
			if (stack[k] != stack[k + 1])
				flips++;
		}

		fout<<"Case #"<<curCase<<": "<<flips<<endl;
		curCase++;
	}

	return 0;
}