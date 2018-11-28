#include<iostream>
#include<string>
using namespace std;

void solve();

int main() {
	int n;
	cin >> n;
	int t = 1;
	string tmp;
	getline(cin, tmp);
	while (n--) {
		cout << "Case #" << t << ": ";
		solve();
		getline(cin, tmp);
		t++;
	}
	return 0;
}

void solve() {
	string line;
	char tttx[4][4];
	char ttto[4][4];
	bool xwin = false, owin = false, draw = false, incomplete = false;
	for (int i = 0; i<4; i++) {
		getline(cin, line);
		//cout << "|" << line << "|" << "\n";
		for (int j = 0; j<4; j++) {
			if (line[j] == '.') {
				incomplete = true;
			}
			tttx[i][j] = line[j] == 'T' ? 'X' : line[j];
			ttto[i][j] = line[j] == 'T' ? 'O' : line[j];
		}
	}
	
	/*
	for (int i = 0; i<4; i++) {
		for (int j = 0; j<4; j++) {
			cout << tttx[i][j];
		}
		cout <<"\n";
	}
	for (int i = 0; i<4; i++) {
		for (int j = 0; j<4; j++) {
			cout << ttto[i][j];
		}
		cout <<"\n";
	}
	*/
	
	// check for X
	if (tttx[0][0] == 'X' && tttx[0][1] == 'X' && tttx[0][2] == 'X' && tttx[0][3] == 'X') xwin = true;
	if (tttx[1][0] == 'X' && tttx[1][1] == 'X' && tttx[1][2] == 'X' && tttx[1][3] == 'X') xwin = true;
	if (tttx[2][0] == 'X' && tttx[2][1] == 'X' && tttx[2][2] == 'X' && tttx[2][3] == 'X') xwin = true;
	if (tttx[3][0] == 'X' && tttx[3][1] == 'X' && tttx[3][2] == 'X' && tttx[3][3] == 'X') xwin = true;
	if (tttx[0][0] == 'X' && tttx[1][0] == 'X' && tttx[2][0] == 'X' && tttx[3][0] == 'X') xwin = true;
	if (tttx[0][1] == 'X' && tttx[1][1] == 'X' && tttx[2][1] == 'X' && tttx[3][1] == 'X') xwin = true;
	if (tttx[0][2] == 'X' && tttx[1][2] == 'X' && tttx[2][2] == 'X' && tttx[3][2] == 'X') xwin = true;
	if (tttx[0][3] == 'X' && tttx[1][3] == 'X' && tttx[2][3] == 'X' && tttx[3][3] == 'X') xwin = true;	
	if (tttx[0][0] == 'X' && tttx[1][1] == 'X' && tttx[2][2] == 'X' && tttx[3][3] == 'X') xwin = true;
	if (tttx[3][0] == 'X' && tttx[2][1] == 'X' && tttx[1][2] == 'X' && tttx[0][3] == 'X') xwin = true;
	
	if (xwin) {
		cout << "X won\n";
		return;
	}
			
	// check for O
	if (ttto[0][0] == 'O' && ttto[0][1] == 'O' && ttto[0][2] == 'O' && ttto[0][3] == 'O') owin = true;
	if (ttto[1][0] == 'O' && ttto[1][1] == 'O' && ttto[1][2] == 'O' && ttto[1][3] == 'O') owin = true;
	if (ttto[2][0] == 'O' && ttto[2][1] == 'O' && ttto[2][2] == 'O' && ttto[2][3] == 'O') owin = true;
	if (ttto[3][0] == 'O' && ttto[3][1] == 'O' && ttto[3][2] == 'O' && ttto[3][3] == 'O') owin = true;
	if (ttto[0][0] == 'O' && ttto[1][0] == 'O' && ttto[2][0] == 'O' && ttto[3][0] == 'O') owin = true;
	if (ttto[0][1] == 'O' && ttto[1][1] == 'O' && ttto[2][1] == 'O' && ttto[3][1] == 'O') owin = true;
	if (ttto[0][2] == 'O' && ttto[1][2] == 'O' && ttto[2][2] == 'O' && ttto[3][2] == 'O') owin = true;
	if (ttto[0][3] == 'O' && ttto[1][3] == 'O' && ttto[2][3] == 'O' && ttto[3][3] == 'O') owin = true;	
	if (ttto[0][0] == 'O' && ttto[1][1] == 'O' && ttto[2][2] == 'O' && ttto[3][3] == 'O') owin = true;
	if (ttto[3][0] == 'O' && ttto[2][1] == 'O' && ttto[1][2] == 'O' && ttto[0][3] == 'O') owin = true;
	
	if (owin) {
		cout << "O won\n";
		return;
	}

	if (incomplete) {
		cout << "Game has not completed\n";
	}
	else {
		cout << "Draw\n";
	}
	
	return;
}
