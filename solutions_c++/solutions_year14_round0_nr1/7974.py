#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main () {
	ifstream fin ("A-small-attempt0.in");
	if (!fin)  // validation
		return 1;
	ofstream fout ("A-small-attempt0.out");
	if (!fout)  // validation
		return 1;

	unsigned int testCases;
	fin >> testCases;
	if (testCases < 0 || testCases > 100)  // validation
		return 1;

	unsigned int ll = 1;
	while (ll <= testCases) {
		unsigned int answer1, answer2;
		fin >> answer1;
		if (answer1 < 0 || answer1 > 4)
			return 1;

		int a1[4][4], a2[4][4];

		for (int i = 0 ; i < 4 ; i++)
			for (int k = 0 ; k < 4 ; k++)
				fin >> a1[i][k];
		
		fin >> answer2;
		if (answer2 < 0 || answer2 > 4)
			return 1;

		for (int i = 0 ; i < 4 ; i++)
			for (int k = 0 ; k < 4 ; k++)
				fin >> a2[i][k];
		
		answer1--;
		answer2--;
		int f1[] = {a1[answer1][0], a1[answer1][1], a1[answer1][2], a1[answer1][3]};
		int f2[] = {a2[answer2][0], a2[answer2][1], a2[answer2][2], a2[answer2][3]};
		int occur = 0;
		int i = 0, k = 0;
		int save = 0;
		bool notSaved = true;
		for (i = 0 ; i < 4 ; i++) {
			for (k = 0 ; k < 4 ; k++) {
				if (f1[i] == f2[k]) {
					occur++;
					if (occur == 1 && notSaved)
						save = k;
					notSaved = false;
					break;
				}
			}	
		}



		if (occur == 1)
			fout << "Case #" << ll << ": " << f2[save] << endl;
		else if (occur > 1)
			fout << "Case #" << ll << ": " << "Bad magician!" << endl;
		else if (occur == 0)
			fout << "Case #" << ll << ": " << "Volunteer cheated!" << endl;
		ll++;
	}
	fout.close ();
	fin.close ();
	return 0;
}