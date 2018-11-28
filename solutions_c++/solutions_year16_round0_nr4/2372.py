// ProblemD.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("D-small-attempt0.in");
	ofstream fout("D-small-attempt0.out");

	int item_count = 0;
	fin >> item_count;

	for (int i = 0; i < item_count; i++)
	{
		int k, c, s;
		fin >> k >> c >> s;

		fout << "Case #" << i + 1 << ":";
		for (int j = 1; j <= s; j++)
			fout << " " << j;

		fout << endl;
	}

    return 0;
}

