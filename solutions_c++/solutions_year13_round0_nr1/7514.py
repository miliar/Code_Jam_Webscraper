#include <iostream>

using namespace std;

#define X_WIN 	352
#define X_WIN_T 348
#define O_WIN 	316
#define O_WIN_T 321

void checkDiagonal(int sum, int n, bool &diagonalWin) {
	if(sum == X_WIN || sum == X_WIN_T) {
		cout << "Case #" << n << ": X won\n";
		diagonalWin = true;
	}
	else if(sum == O_WIN || sum == O_WIN_T) {
		cout << "Case #" << n << ": O won\n";
		diagonalWin = true;
	}
}

void checkHorizontal(int sum, int n, bool &horizontWin) {
	if(sum == X_WIN || sum == X_WIN_T) {
		cout << "Case #" << n << ": X won\n";
		horizontWin = true;
	}
	else if(sum == O_WIN || sum == O_WIN_T) {
		cout << "Case #" << n << ": O won\n";
		horizontWin = true;
	}
}

void checkVertical(int sum, int n, bool &verticalWin) {
	if(sum == X_WIN || sum == X_WIN_T) {
		cout << "Case #" << n << ": X won\n";
		verticalWin = true;
	}
	else if(sum == O_WIN || sum == O_WIN_T) {
		cout << "Case #" << n << ": O won\n";
		verticalWin = true;
	}
}


int main(int argc, const char* argv[]) {

	int numOfTest;
	cin >> numOfTest;
	char board[4][4];
	for(int n=1; n<=numOfTest; n++) {
		bool gameNotOver = false;
		bool diagonalWin = false;
		bool verticalWin = false;
		bool horizontWin = false;

		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				cin >> board[i][j];
				if(board[i][j] == '.')
					gameNotOver = true;
			}
		}
		//check this game
		
			int sum = 0;
			//check horizontal
			sum = board[0][0]+board[0][1]+board[0][2]+board[0][3];
			checkHorizontal(sum, n, horizontWin);
			sum = board[1][0]+board[1][1]+board[1][2]+board[1][3];
			checkHorizontal(sum, n, horizontWin);
			sum = board[2][0]+board[2][1]+board[2][2]+board[2][3];
			checkHorizontal(sum, n, horizontWin);
			sum = board[3][0]+board[3][1]+board[3][2]+board[3][3];
			checkHorizontal(sum, n, horizontWin);

			//check vertical
			if(!horizontWin) {
				sum = board[0][0]+board[1][0]+board[2][0]+board[3][0];
				checkVertical(sum, n, verticalWin);
				sum = board[0][1]+board[1][1]+board[2][1]+board[3][1];
				checkVertical(sum, n, verticalWin);
				sum = board[0][2]+board[1][2]+board[2][2]+board[3][2];
				checkVertical(sum, n, verticalWin);
				sum = board[0][3]+board[1][3]+board[2][3]+board[3][3];
				checkVertical(sum, n, verticalWin);
			}
			//check diagonal
			if(!horizontWin && !verticalWin) {
				sum = board[0][0]+board[1][1]+board[2][2]+board[3][3];
				checkDiagonal(sum, n, diagonalWin);
				sum = board[0][3]+board[1][2]+board[2][1]+board[3][0];
				checkDiagonal(sum, n, diagonalWin);
			}
			if(!diagonalWin && !horizontWin && !verticalWin && !gameNotOver) {
				cout << "Case #" << n << ": Draw\n";
			} else if(!diagonalWin && !horizontWin && !verticalWin && gameNotOver) {
				cout << "Case #" << n << ": Game has not completed\n";
			}
	}
	return 0;
}


