#include <iostream>
#include <string>

using namespace std;
int T;
char bo[4][4];

int checkWin(char b) {
	int cs = 0, cb = 0;
	for (int i = 0; i < 4; i++) {
		int cv = 0, ch = 0;
		for (int j = 0; j < 4; j++) {
			if(bo[i][j] == b || bo[i][j] == 'T')
				ch++;
			if(bo[j][i] == b || bo[j][i] == 'T')
				cv++;
		}
		if(cv==4 || ch ==4)
			return 1;

		if(bo[i][i] == b || bo[i][i] == 'T')
			cs++;
		if(bo[i][3-i] == b || bo[i][3-i] == 'T')
			cb++;
	}

	if(cb==4 || cs ==4)
		return 1;
	return 0;
}


int main() {
	string s;
	cin >> T;
	for (int p = 1; p <= T; p++) {
		int em = 0;

		for (int i = 0; i < 4; i++) {
			cin >> s;
			for (int j = 0; j < 4; j++) {
				bo[i][j]=s.at(j);
				if(bo[i][j] == '.')
					em = 1;
			}
		}
		//cin >> s;

		cout << "Case #" << p << ": ";
	
		if(checkWin('X'))
			cout << "X won";
		else if(checkWin('O'))
			cout << "O won";
		else if(em == 0)
			cout << "Draw";
		else
			cout << "Game has not completed";
		
		cout << endl;
	}
}