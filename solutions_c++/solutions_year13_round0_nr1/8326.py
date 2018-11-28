// Pooja Ahuja
// Google CodeJam

#include <iostream>
#include <cstdlib>
using namespace std;

#define INC	0
#define DRAW	1
#define XWON	2
#define OWON	3

bool isEqual(char x, char y) {
	if (x == '.' || y == '.')
		return false;
	else if (x == y || x == 'T' || y == 'T')
		return true;
	else
		return false;
}

int main()
{
	int T, result;
	char line[4][5], res[4][4];
	bool xw, ow, dr, pdiag, sdiag;
	cin >> T;
	cin.get();

	for (int testcase = 1; testcase <= T; ++testcase) {
		result = INC;
		dr = true;

		for (int i = 0; i < 4; ++i) {
			cin.getline(line[i], 5);
			if (result != INC)
				continue;

			xw = ow = true;
			for (int j = 0; j < 4 && (dr || xw || ow); ++j) {
				if (line[i][j] != 'X' && line[i][j] != 'T')
					xw = false;
				if (line[i][j] != 'O' && line[i][j] != 'T')
					ow = false;
				if (line[i][j] == '.')
					dr = false;
			}

			if (xw)
				result = XWON;
			else if (ow)
				result = OWON;
		}

		if (result == INC) {
			pdiag = sdiag = true;
			for (int i = 1; i < 4; ++i) {
				if (!isEqual(line[i][i], line[i-1][i-1]))
					pdiag = false;
				if (!isEqual(line[i][3-i], line[i-1][4-i]))
					sdiag = false;
			}
			
			if (!pdiag && !sdiag) {
				for (int i = 1; i < 4; ++i) {
					for (int j = 0; j < 4; ++j) {
						if (!isEqual(line[i][j], line[i-1][j]))
							line[i][j] = '.';
					}
				}
				
				for (int i = 0; i < 4; ++i) {
					if (line[3][i] != '.') {
						result = line[3][i] == 'X' ? XWON : OWON;
						break;
					}
				}
			} else if (pdiag) {
				if (line[3][3] == 'T')
					line[3][3] = line[2][2];
				result = line[3][3] == 'X' ? XWON : OWON;
			} else if (sdiag) {
				if (line[3][0] == 'T')
					line[3][0] = line[2][1];
				result = line[3][0] == 'X' ? XWON : OWON;
			}
			
			if (result == INC && dr)
				result = DRAW;
		}

		cout << "Case #" << testcase << ": ";
		switch (result) {
		case XWON:
			cout << "X won" << endl;
			break;
		case OWON:
			cout << "O won" << endl;
			break;
		case DRAW:
			cout << "Draw" << endl;
			break;
		case INC:
			cout << "Game has not completed" << endl;
			break;
		}
		cin.get();
	}
}
