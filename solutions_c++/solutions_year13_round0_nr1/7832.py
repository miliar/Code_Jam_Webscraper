#include <iostream>
#include <cstdlib>
using namespace std;

//	Alex Lenail
//	Google Code Jam
//	4 / 13 / 13

class game {

	public:

		game();

		char check();


	private:

		char board[4][4];

		char check_h();

		char check_v();

		char check_d();

		bool board_is_full();

};



game::game() {

	char input;

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {

			cin >> input;
			board[i][j] = input;

		}
	}

}

char game::check() {

	char h = check_h();

	if (h == 'X' || h == 'O') {return h;}

	char v = check_v();
	
	if (v == 'X' || v == 'O') {return v;}

	char d = check_d();

	if (d == 'X' || d == 'O') {return d;}

// ===== We can assume no player has won. =====

	if (board_is_full()) {return 'D';}

	else {return 'U';}

}

char game::check_h() {

	for (int i = 0; i < 4; i++) {

		if ( (  (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][2] == board[i][3]) ||
				(board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][3] == 'T') ||
				(board[i][0] == board[i][1] && board[i][1] == board[i][3] && board[i][2] == 'T') ||
				(board[i][0] == board[i][2] && board[i][2] == board[i][3] && board[i][1] == 'T') ||
				(board[i][1] == board[i][2] && board[i][2] == board[i][3] && board[i][0] == 'T')  )
			 &&
				(board[i][0] != '.') && (board[i][1] != '.') && 
				(board[i][2] != '.') && (board[i][3] != '.') ) {

			if (board[i][0] != 'T') {return board[i][0];} else {return board[i][1];}

		}

	}

	return 'N';

}

char game::check_v() {

	for (int j = 0; j < 4; j++) {

		if ( (  (board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[2][j] == board[3][j]) ||
				(board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[3][j] == 'T') ||
				(board[0][j] == board[1][j] && board[1][j] == board[3][j] && board[2][j] == 'T') ||
				(board[0][j] == board[2][j] && board[2][j] == board[3][j] && board[1][j] == 'T') ||
				(board[1][j] == board[2][j] && board[2][j] == board[3][j] && board[0][j] == 'T')  )
			&&
				(board[0][j] != '.') && (board[1][j] != '.') && 
				(board[2][j] != '.') && (board[3][j] != '.') ) {

			if (board[0][j] != 'T') {return board[0][j];} else {return board[1][j];}

		}

	}

	return 'N';

}

char game::check_d() {

	if ( (  (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == board[3][3]) ||
			(board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[3][3] == 'T') ||
			(board[0][0] == board[1][1] && board[1][1] == board[3][3] && board[2][2] == 'T') ||
			(board[0][0] == board[2][2] && board[2][2] == board[3][3] && board[1][1] == 'T') ||
			(board[1][1] == board[2][2] && board[2][2] == board[3][3] && board[0][0] == 'T')  )
		&&
			(board[0][0] != '.') && (board[1][1] != '.') && 
			(board[2][2] != '.') && (board[3][3] != '.') ) {

			if (board[0][0] != 'T') {return board[0][0];} else {return board[1][1];}

	}

	if ( (  (board[0][3] == board[1][2] && board[1][2] == board[2][1] && board[2][1] == board[3][0]) ||
			(board[0][3] == board[1][2] && board[1][2] == board[2][1] && board[2][1] && board[3][0] == 'T') ||
			(board[0][3] == board[1][2] && board[1][2] == board[3][0] && board[3][0] && board[2][1] == 'T') ||
			(board[0][3] == board[2][1] && board[2][1] == board[3][0] && board[3][0] && board[1][2] == 'T') ||
			(board[1][2] == board[2][1] && board[2][1] == board[3][0] && board[3][0] && board[0][3] == 'T')  )
		&&
			(board[1][2] != '.') && (board[2][1] != '.') && 
			(board[0][3] != '.') && (board[3][0] != '.') ) {

			if (board[3][0] != 'T') {return board[3][0];} else {return board[0][3];}

	}

	return 'N';

}

bool game::board_is_full() {

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {

			if (board[i][j] == '.') {return false;}

		}
	}

	return true;

}



int main() {

	int num; 

	cin >> num; if (num > 1000) {cout << "Error: invalid input"; exit(1);}

	game* games[num];

	for (int i = 0; i < num; i++) {

		games[i] = new game;

	}

	char result;

	for (int i = 0; i < num; i++) {

		result = games[i] -> check();
		cout << "Case #" << i+1 << ": ";

		if (result == 'X' || result == 'O') {cout << result << " won" << endl;}

		else if (result == 'D') {cout << "Draw" << endl;}

		else if (result == 'U') {cout << "Game has not completed" << endl;}

		else {cout << "ERROR: I made a whoopsie." << endl;}

	}

	return 0;

}
