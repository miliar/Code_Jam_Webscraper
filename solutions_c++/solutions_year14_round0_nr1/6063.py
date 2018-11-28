#include <iostream>
#include <fstream>

using namespace std;

int test_cases, tc;
int was[20];

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	fin >> test_cases;

	int row, x;

	for (tc = 1; tc <= test_cases; tc++) {
		memset(was, 0, sizeof(was));
		for (int k=0; k<2; k++) {			
			fin >> row;
			for (int i=1; i<=4; i++) {
				for (int j=0; j<4; j++) {
					fin >> x;
					if (i == row)
						was[x]++;
				}
			}
		}

		int res = -1;
		int cnt = 0;
		for (int i=1; i<=16; i++) {			
			if (was[i] == 2) {
				res = i;
				cnt++;
			}
		}

		fout << "Case #" << tc << ": ";
		
		if (cnt == 1)
			fout << res << endl;
		else if (cnt > 1)
			fout << "Bad magician!" << endl;
		else
			fout << "Volunteer cheated!" << endl;
	}

	return 0;
}