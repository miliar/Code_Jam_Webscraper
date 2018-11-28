#include <iostream>
#include <fstream>

using namespace std;
char board[4][4];

bool winner(char player){
	char enemy;
	if (player == 'O') enemy = 'X';
	else enemy = 'O';

	// Each line
	for (int y = 0; y < 4; y++){
		bool win = true;
		for (int x = 0; x < 4; x++){
			if (board[x][y] == enemy || board[x][y] == '.'){
				win = false;
				break;
			}
		}
		if (win){
			//cout << "match line " << y << endl;
			return true;
		}
	}

	// Each column
	for (int x = 0; x < 4; x++){
		bool win = true;
		for (int y = 0; y < 4; y++){
			if (board[x][y] == enemy || board[x][y] == '.'){
				win = false;
				break;
			}
		}
		if (win){
			//cout << "match column " << x << endl;
			return true;
		}
	}

	// Diagonals
	bool win = true;
	for (int i = 0; i < 4; i++){
		if (board[i][i] == enemy || board[i][i] == '.'){
			win = false;
			break;
		}
	}
	if (win){
		//cout << "match diagonal 1" << endl;
		return true;
	}

	win = true;
	int x, y;
	for (y = 3, x = 0; x < 4; y--, x++){
		if (board[x][y] == enemy || board[x][y] == '.'){
			win = false;
			break;
		}
	}
	if (win){
		//cout << "match diagonal 2" << endl;
		return true;
	}

	return false;
}

bool draw(){
	for (int y = 0; y < 4; y++){
		for (int x = 0; x < 4; x++){
			if (board[x][y] == '.'){
				return false;
			}
		}
	}
	return true;
}

int main(){
	ifstream input("input.txt");
	if (!input){
		cerr << "Failed to open file";
		return 1;
	}
	ofstream output("output.txt");
	
	int lines;
	input >> lines;


	char nl;

	for (int i = 0; i < lines; i++){
		input >> board[0][0];
		input >> board[1][0];
		input >> board[2][0];
		input >> board[3][0];
		input >> board[0][1];
		input >> board[1][1];
		input >> board[2][1];
		input >> board[3][1];
		input >> board[0][2];
		input >> board[1][2];
		input >> board[2][2];
		input >> board[3][2];
		input >> board[0][3];
		input >> board[1][3];
		input >> board[2][3];
		input >> board[3][3];

		output << "Case #" << (i + 1) << ": ";

		if (winner('X')){
			output << "X won";
		}else if (winner('O')){
			output << "O won";
		}else if (draw()){
			output << "Draw";
		}else{
			output << "Game has not completed";
		}

		output << endl;
	}



	output.close();
	input.close();

	system("pause");

	return 0;
}