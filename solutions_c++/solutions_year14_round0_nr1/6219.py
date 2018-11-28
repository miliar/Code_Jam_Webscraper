#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ofstream fout("A-small-attempt0.out");
	ifstream fin ("A-small-attempt0.in");

	int t; 	fin >> t;

	for (int i = 1; i <= t; i++)
	{
		int r1, r2, aR1[4], aR2[4], count = 0, result, ignore;
		fin >> r1;
		for (int i1 = 0; i1 < 4; i1++)
		for (int i2 = 0; i2 < 4; i2++){ if (i1 == r1 - 1) fin >> aR1[i2]; else fin >> ignore; }
		fin >> r2;
		for (int i1 = 0; i1 < 4; i1++)
		for (int i2 = 0; i2 < 4; i2++){ if (i1 == r2 - 1) fin >> aR2[i2]; else fin >> ignore;}

		for (int i1 = 0; i1 < 4; i1++)
		{
			for (int i2 = 0; i2 < 4; i2++) if (aR2[i2] == aR1[i1]) { result = aR1[i1]; count++; }
			if (count > 1) break;
		}
		fout << "Case #" << i << ": ";
		if (count == 1)  fout << result << endl;
		else if (count > 1) fout << "Bad magician!" << endl;
		else fout << "Volunteer cheated!" << endl;
	}

	fout.close();
	fin.close();
	return 0;
}
