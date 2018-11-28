#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <fstream>
#include <iostream>
#include <limits>

using namespace std;

int main()
{
	ifstream inputfile;
	ofstream outputfile;

	// char *inputfilename = argv[2];
	inputfile.open("B-large.in");
	// inputfile.open(inputfilename);
	outputfile.open("output.txt");
	outputfile.clear();

	int cases;
	int count = 1;
	// input case number
	inputfile >> cases;

	string s;

	while (count <= cases)
	{
		inputfile >> s;
		char cur = s[0];
		int res = 0;
		for (int i = 1; i < s.length(); i++)
		{
			if (s[i] != cur)
			{
				res++;
				cur = s[i];
			}
		}
		if (cur == '-')
			res++;
		outputfile << "Case #" << count << ": " << res << endl;
		count++;
	}

	// system("pause");
	return 0;
}