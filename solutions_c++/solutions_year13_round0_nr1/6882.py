#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<char> > Matrix;

bool read(Matrix& m) {
	bool comp = true;
	char in;
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++) {
			cin >> in;
			if (in == '.') comp = false;
			m[i][j] = in;
		}
	return comp;	
}

bool vertical(const Matrix& m, int j, char c) {
	if ((m[0][j] == c or m[0][j] == 'T') and (m[1][j] == c or m[1][j] == 'T') and (m[2][j] == c or m[2][j] == 'T') and (m[3][j] == c or m[3][j] == 'T')) return true;
	return false;
}

bool horizontal(const Matrix& m, int i, char c) {
	if ((m[i][0] == c or m[i][0] == 'T') and (m[i][1] == c or m[i][1] == 'T') and (m[i][2] == c or m[i][2] == 'T') and (m[i][3] == c or m[i][3] == 'T')) return true;
	return false;
}

bool wins(const Matrix& m) {
	if ((m[0][0] == 'X' or m[0][0] == 'T') and (m[1][1] == 'X' or m[1][1] == 'T') and (m[2][2] == 'X' or m[2][2] == 'T') and (m[3][3] == 'X' or m[3][3] == 'T')) return true;
	if ((m[3][0] == 'X' or m[3][0] == 'T') and (m[2][1] == 'X' or m[2][1] == 'T')  and (m[1][2] == 'X' or m[1][2] == 'T') and (m[0][3] == 'X' or m[0][3] == 'T'))  return true;
	for (int j=0; j<4; j++) if (vertical(m,j,'X')) return true;
	for (int i=0; i<4; i++) if (horizontal(m,i,'X')) return true;
	return false;
}

bool loses(const Matrix& m) {
	if ((m[0][0] == 'O' or m[0][0] == 'T') and (m[1][1] == 'O' or m[1][1] == 'T') and (m[2][2] == 'O' or m[2][2] == 'T') and (m[3][3] == 'O' or m[3][3] == 'T')) return true;
	if ((m[3][0] == 'O' or m[3][0] == 'T') and (m[2][1] == 'O' or m[2][1] == 'T')  and (m[1][2] == 'O' or m[1][2] == 'T') and (m[0][3] == 'O' or m[0][3] == 'T'))  return true;
	for (int j=0; j<4; j++) if (vertical(m,j,'O')) return true;
	for (int i=0; i<4; i++) if (horizontal(m,i,'O')) return true;
	return false;
}

int main() {
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";
		Matrix m(4,vector<char>(4));
		bool complete = read(m);
		if (wins(m)) cout << "X won" << endl;
		else if (loses(m)) cout << "O won" << endl;
		else {
			if (!complete) cout << "Game has not completed" << endl;
			else cout << "Draw" << endl;
		}
	}	
}
