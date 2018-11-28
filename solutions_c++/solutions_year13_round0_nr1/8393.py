#include <iostream>

using namespace std;

int judge(char ** board) {
	int emptyNum = 0;
	int i, j;
	
	for(i = 0; i < 4; i++) {
		char cur = board[i][0];
		if(cur == 'T') {
			cur = board[i][1];
		}
		if(cur == '.') {
			emptyNum ++;
			continue;
		}
		bool won = true;
		for(j = 1; j < 4; j++) {
			if(board[i][j] != 'T' && board[i][j] != cur) {
				won = false;
			}
			if(board[i][j] == '.') {
				emptyNum ++;
			}
		}
		if(won) {
			if(cur == 'X') {
				return 1;
			} else {
				return 2;
			}
		}
	}
	
	for(i = 0; i < 4; i++) {
		char cur = board[0][i];
		if(cur == 'T') {
			cur = board[1][i];
		}
		if(cur == '.') {
			emptyNum ++;
			continue;
		}
		bool won = true;
		for(j = 1; j < 4; j++) {
			if(board[j][i] != 'T' && board[j][i] != cur) {
				won = false;
			}
			if(board[j][i] == '.') {
				emptyNum ++;
			}
		}
		if(won) {
			if(cur == 'X') {
				return 1;
			} else {
				return 2;
			}
		}
	}
	
	if((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T')) {
		return 1;
	}
	if((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T')) {
		return 2;
	}
	
	if(emptyNum == 0) {
		return 3;
	} else {
		return 4;
	}
}

int main() {

	int number;
	cin>>number;
	int origin = number;
	
	while(number > 0) {
		
		number --;
		char board[4][4];
		
		int i, j;
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				cin>>board[i][j];
			}
		//	cin.get();
		}
		
		if(number > 0) {
		//	cin.get();
		}
		
		cout<<"Case #"<<origin-number<<": ";
		int res = judge(board);
		if( res == 1) {
			cout<<"X won"<<endl;
		}
		if(res == 2) {
			cout<<"O won"<<endl;
		}
		if(res == 3) {
			cout<<"Draw"<<endl;
		}
		if(res == 4) {
			cout<<"Game has not completed"<<endl;
		}
	}
	
	return 0;
}