#include<iostream>
using namespace std;

void check(int* x, int* o, char source);
char win(char a, char b, char c, char d);
char whoWin();

char source[4][4];
int main() {
	int num;
	cin >> num;
	for(int a = 0; a < num; a++) {	
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> source[i][j];
			}
		}
		// who won
		char winner = whoWin();
		if(winner != 'N') {
			cout << "Case #" << a + 1 << ": " << winner << " won" << endl;
		}else {
		// done?
		bool done = true;
		for(int i = 0; i < 4 && done; i++) {
			for(int j = 0; j < 4 && done; j++) {
				if(source[i][j] == '.') {
					cout << "Case #" << a + 1 << ": " << "Game has not completed" << endl;
					done = false;
				}
			}
		}
		if(done) {
			cout << "Case #" << a + 1 << ": " << "Draw" << endl;
		}
		}
	}
}

char win(char a, char b, char c, char d) {
	int x = 0, o = 0;
	int *p = &x, *q = &o;

	check(p, q, a);
	check(p, q, b);
	check(p, q, c);
	check(p, q, d);

	if(a == 'T' || b == 'T' || c == 'T' || d == 'T') {
		if(x == 3) {return 'X';}
		if(o == 3) {return 'O';}
	}else {
		if(x == 4) {return 'X';}
		if(o == 4) {return 'O';}
	}

	return 'N';
}


void check(int* x, int* o, char source) {
	if(source == 'X') { *x += 1;}
	if(source == 'O') { *o += 1;}
}

char whoWin() {
	char winner;
	for(int i = 0; i < 4; i++) {
		winner = win(source[i][0], source[i][1], source[i][2], source[i][3]);
		if(winner != 'N') {
			return winner;
		}
	}
	for(int i = 0; i < 4; i++) {
		winner = win(source[0][i], source[1][i], source[2][i], source[3][i]);
		if(winner != 'N') {
			return winner;
		}
	}
	
	winner = win(source[0][0], source[1][1], source[2][2], source[3][3]);
	if(winner != 'N') {
		return winner;
	}
	winner = win(source[0][3], source[1][2], source[2][1], source[3][0]);
	if(winner != 'N') {
		return winner;
	}
	return 'N';
}
