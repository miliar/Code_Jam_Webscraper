#include <iostream>
using namespace std;

char board[4][4];

char win(char in[4]){
	int O = 0;
	int X = 0;
	int T = 0;

	for(int i = 0; i < 4; i++){
		if(in[i] == 'X'){ X++; }
		if(in[i] == 'O'){ O++; }
		if(in[i] == 'T'){ T++; }
	}

	if(X == 4 || (X==3&&T==1)){
		return 'X';
	} else if(O == 4 || (O==3&&T==1)){
		return 'O';
	} else {
		return '-';
	}
}

void JeMoeder(int caseNr){
	cout << "Case #" << caseNr << ": ";

	// read in board and check if completed
	bool completed = true;
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			cin >> board[i][j];
			if(board[i][j] == '.'){
				completed = false;
			}
		}
	}

	// check every row and colomn
	for(int i = 0; i < 4; i++){
		char row[4]; char colomn[4]; 
		for(int j = 0; j < 4; j++){
			row[j] = board[i][j];
			colomn[j] = board[j][i];
		}

		char winRow = win(row);
		char winColomn = win(colomn);

		if(winRow == 'X' || winColomn == 'X'){
			cout << "X won" << endl; return;
		} else if(winRow == 'O' || winColomn == 'O'){
			cout << "O won" << endl; return;
		}
	}

	// check diagornal
	char dia1[4]; char dia2[4];
	for(int i = 0; i < 4; i++){
		dia1[i] = board[i][i];
		dia2[i] = board[3-i][i];
	}

	char winDia1 = win(dia1);
	char winDia2 = win(dia2);

	if(winDia1 == 'X' || winDia2 == 'X'){
		cout << "X won" << endl; return;
	} else if(winDia1 == 'O' || winDia2 == 'O'){
		cout << "O won" << endl; return;
	}

	// no winner
	if(completed){
		cout << "Draw" << endl;
	} else {
		cout << "Game has not completed" << endl;
	}
}

int main(){
	int count; cin >> count;
	for(int i = 1; i <= count; i++){
		JeMoeder(i);
	}
}