#include <fstream>

using namespace std;

int f[20];

main () {
	ifstream fin ("A.in");
	ofstream fout ("A.out");
	int T;
	fin >> T;
	for (int tr = 1; tr <= T; tr++) {
		for (int i = 1; i <= 16; i++) f[i] = 0;
		int a, b;
		fin >> a;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				int tmp;
				fin >> tmp;
				if (i == a)  f[tmp]++;
			}
		fin >> b;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				int tmp;
				fin >> tmp;
				if (i == b)  f[tmp]++;
			}
		int ans = 0;
		for (int i = 1; i <= 16; i++)
			if (f[i] == 2) {
				if (ans != 0) {
					fout << "Case #" << tr << ": Bad magician!" << endl;
					goto nexttr;
				}
				ans = i;
			}
		if (ans == 0) {
			fout << "Case #" << tr << ": Volunteer cheated!" << endl;
			goto nexttr;
		}
		fout << "Case #" << tr << ": " << ans << endl;
		nexttr:;
	}
}
