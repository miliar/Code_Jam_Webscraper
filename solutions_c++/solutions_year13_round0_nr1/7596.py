#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char a[4][4];
bool p;
int rans;

int main()
{
	int T;
	cin >> T;
	int x, y;
	char tmp = getchar();
	for (int t = 1; t <= T; t ++) {
		p = 0;
		x = y = -1;
	//	char tmp = getchar();
		//t = 0;
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				cin >> a[i][j];
				if (a[i][j] == '.') p = 1;
				if (a[i][j] == 'T') x = i, y = j;
			}
			tmp = getchar();
		}
		rans = 0;
		if (x !=-1 && y != -1)
			a[x][y] = 'X';
		///
	//	for (int i = 0; i < 4; i ++) {
	//		for (int j = 0; j < 4; j ++) cout << a[i][j];
	//		cout << endl;
	//	}
		for (int i = 0; i < 4; i ++) {
			if ((a[i][0] == a[i][1]) && (a[i][1] == a[i][2]) && (a[i][2] == a[i][3]) && (a[i][0] == 'X')) { rans = 1; break;}
			else if ((a[i][0] == a[i][1]) && (a[i][1] == a[i][2]) && (a[i][2] == a[i][3]) && (a[i][0] ==  'O')) { rans = 2; break;}
		}
		for (int i = 0; i < 4 && !rans; i ++) {
			if ((a[0][i] == a[1][i]) && (a[1][i] == a[2][i]) && (a[2][i] == a[3][i]) && (a[0][i] =='X')) {rans = 1; break;}
			else if((a[0][i] == a[1][i]) && (a[1][i] == a[2][i]) && (a[2][i] == a[3][i]) && (a[0][i] == 'O')) {rans = 2; break;}
		}
		if ((a[0][0] == a[1][1]) && (a[1][1] == a[2][2]) && (a[2][2] == a[3][3])) {
			if (a[0][0] == 'X') rans = 1;
			if (a[0][0] == 'O') rans = 2;
		}
		if ((a[0][3] == a[1][2]) && (a[1][2] == a[2][1]) && (a[2][1] == a[3][0])) {
			if (a[0][3] == 'X') rans = 1;
			if (a[0][3] == 'O') rans = 2;
		}
		if (x != -1 && y != -1)
			a[x][y] = 'O';
	//	for (int i = 0; i < 4; i ++) {
	//		for (int j = 0; j < 4; j ++) cout << a[i][j];
	//		cout << endl;
	//	}
		for (int i = 0; i < 4; i ++) {
			if ((a[i][0] == a[i][1]) && (a[i][1] == a[i][2]) && (a[i][2] == a[i][3]) && (a[i][0] == 'X')) { rans = 1; break;}
			else if ((a[i][0] == a[i][1]) && (a[i][1] == a[i][2]) && (a[i][2] == a[i][3]) && (a[i][0] ==  'O')) { rans = 2; break;}
		}
		for (int i = 0; i < 4 && !rans; i ++) {
			if ((a[0][i] == a[1][i]) && (a[1][i] == a[2][i]) && (a[2][i] == a[3][i]) && (a[0][i] =='X')) {rans = 1; break;}
			else if((a[0][i] == a[1][i]) && (a[1][i] == a[2][i]) && (a[2][i] == a[3][i]) && (a[i][i] == 'O')) {rans = 2; break;}
		}
		if ((a[0][0] == a[1][1]) && (a[1][1] == a[2][2]) && (a[2][2] == a[3][3])) {
			if (a[0][0] == 'X') rans = 1;
			if (a[0][0] == 'O') rans = 2;
		}
		if ((a[0][3] == a[1][2]) && (a[1][2] == a[2][1]) && (a[2][1] == a[3][0])) {
			if (a[0][3] == 'X') rans = 1;
			if (a[0][3] == 'O') rans = 2;
		}
		if (rans == 1) cout << "Case #" << t << ": X won\n";
		else if (rans == 2) cout << "Case #" << t << ": O won\n";
		else if (rans == 0 && p) cout << "Case #" << t << ": Game has not completed\n";
		else cout << "Case #" << t << ": Draw\n";
	}
	return 0;
}

