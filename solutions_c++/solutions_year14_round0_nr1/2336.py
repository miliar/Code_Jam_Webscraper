#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int a[4][4], b[4][4];

int main() {
	int t, c1, c2;
	ifstream fin ("A-small-attempt4.in");
	ofstream fout ("1.txt");
	fin >> t;
	for (int k = 1; k <= t; k++) {
		fin >> c1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
					fin >> a[i][j];
		fin >> c2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
					fin >> b[i][j];
		int e = 0, ans = -1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a[c1-1][i] == b[c2-1][j]) {
					e++;
					if (e == 1)
						ans = a[c1-1][i];
				}
		switch (e) {
			case 0 :	//printf("Case #%d: Volunteer cheated!\n", k);
						fout << "Case #" << k << ": Volunteer cheated!\n";
						break;
			case 1 :	//printf("Case #%d: %d\n", k, ans);
						fout << "Case #" << k << ": " << ans << "\n";
						break;
			default :	//printf("Case #%d: Bad magician!\n", k);
						fout << "Case #" << k << ": Bad magician!\n";
						break;
		}
	}
}