//============================================================================
// Name        : Omino.cpp
//============================================================================


#include <iostream>
#include <fstream>

using namespace std;

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int a[4][4][4];
	fstream f;
	f.open("testcases.txt", ios::in);
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				int s;
				f >> s >> s >> s;
				f >> a[i][j][k];
			}
		}
	}
	f.close();

	ifstream in("in.txt");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		int x, r, c;
		cin >> x >> r >> c;
		x--; r--; c--;
		if(a[x][r][c]) {
			cout << "RICHARD";
		}
		else {
			cout << "GABRIEL";
		}

		cout << '\n';
	}

	in.close();
	out.close();

	return 0;

}
