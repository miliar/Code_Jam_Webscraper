#include <iostream>

using namespace std;

int main() {
	int T,i,j,winner(-1),g;
	string line[4];
	cin >> T;
	for(i = 0; i < T; i++) {
		winner = -1;
		for(j = 0; j < 4; j++) cin >> line[j];

		for(j = 0; j < 4; j++) for(g = 0; g < 4; g++) if(line[j][g] == '.') { winner = 2; break; }

		//X
		for(j = 0; j < 4; j++)
		if((line[j][0] == 'X' || line[j][0] == 'T') && (line[j][1] == 'X' || line[j][1] == 'T') && (line[j][2] == 'X' || line[j][2] == 'T') && (line[j][3] == 'X' || line[j][3] == 'T')) winner = 0;

		for(j = 0; j < 4; j++)
		if((line[0][j] == 'X' || line[0][j] == 'T') && (line[1][j] == 'X' || line[1][j] == 'T') && (line[2][j] == 'X' || line[2][j] == 'T') && (line[3][j] == 'X' || line[3][j] == 'T')) winner = 0;

		if((line[0][0] == 'X' || line[0][0] == 'T') && (line[1][1] == 'X' || line[1][1] == 'T') && (line[2][2] == 'X' || line[2][2] == 'T') && (line[3][3] == 'X' || line[3][3] == 'T')) winner = 0;
		if((line[0][3] == 'X' || line[0][3] == 'T') && (line[1][2] == 'X' || line[1][2] == 'T') && (line[2][1] == 'X' || line[2][1] == 'T') && (line[3][0] == 'X' || line[3][0] == 'T')) winner = 0;

		//O
		for(j = 0; j < 4; j++)
		if((line[j][0] == 'O' || line[j][0] == 'T') && (line[j][1] == 'O' || line[j][1] == 'T') && (line[j][2] == 'O' || line[j][2] == 'T') && (line[j][3] == 'O' || line[j][3] == 'T')) winner = 1;

		for(j = 0; j < 4; j++)
		if((line[0][j] == 'O' || line[0][j] == 'T') && (line[1][j] == 'O' || line[1][j] == 'T') && (line[2][j] == 'O' || line[2][j] == 'T') && (line[3][j] == 'O' || line[3][j] == 'T')) winner = 1;

		if((line[0][0] == 'O' || line[0][0] == 'T') && (line[1][1] == 'O' || line[1][1] == 'T') && (line[2][2] == 'O' || line[2][2] == 'T') && (line[3][3] == 'O' || line[3][3] == 'T')) winner = 1;
		if((line[0][3] == 'O' || line[0][3] == 'T') && (line[1][2] == 'O' || line[1][2] == 'T') && (line[2][1] == 'O' || line[2][1] == 'T') && (line[3][0] == 'O' || line[3][0] == 'T')) winner = 1;

		cout << "Case #" << i+1 << ": ";
		if(winner == -1) {
			cout << "Draw";
		}
		else if(winner == 0) {
			cout << "X won";
		}
		else if(winner == 1) {
			cout << "O won";
		}
		else if(winner == 2) {
			cout << "Game has not completed";
		}
		cout << endl;
	}
	return 0;
}