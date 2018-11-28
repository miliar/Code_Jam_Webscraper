
#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int cases, k, c, s;

	fin >> cases;
	for (int t = 1; t <= cases; t++) {

		fin >> k >> c >> s;
		fout << "Case #" << t << ": ";

		if (s == k) {
			for (int i = 0; i < k; i++)
				fout << i + 1 << " ";
			fout << endl;
		}
	}

	fin.close();
	fout.close();
	return 0;
}
