#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

string checkGame(char inputs[][4], int gameCount);

int main() {
	//gets filename
	string fname;
	getline(cin, fname);
	
	//reads file and grabs number of games
	string number;
	ifstream input(fname.c_str());
	ofstream output("output.txt");
	getline(input, number);
	int numGames = atoi(number.c_str());
	
	//storage for input
	string inputs[numGames][4];
	char game[4][4];
	
	//takes input and checks games
	for (int gameCount = 0; gameCount < numGames; gameCount++) {
		for (int line = 0; line < 4; line++) {
			//first array stores all input
			getline(input, inputs[gameCount][line]);
			//a second array is made to represent an individual game
			for (int index = 0; index < 4; index++) {
				game[line][index] = inputs[gameCount][line][index];
			}
		}
		getline(input, number); //throws away empty lines
		output << checkGame(game, gameCount);
	}
	
	//closes file and returns
	input.close();
	output.close();
	return 1;
}

//checks who won the game
string checkGame(char game[][4], int gameCount) {
	//setup output string
	stringstream caseNum;
	caseNum << "Case #" << (gameCount + 1) << ": ";
	string X = caseNum.str() + "X won\n";
	string O = caseNum.str() + "O won\n";
	string I = caseNum.str() + "Game has not completed\n";
	string D = caseNum.str() + "Draw\n";
	
	//counters	
	int xHorizontal = 0;
	int oHorizontal = 0;
	int xVertical = 0;
	int oVertical = 0;
	int xDiagonal = 0;
	int oDiagonal = 0;
	int xDiagonalInverse = 0;
	int oDiagonalInverse = 0;
	int incomplete = 0;
	
	//checks the game array for horizontal, vertical, and diagonal wins
	for (int line = 0; line < 4; line++) {
		if (game[line][line] == 'X' || game[line][line] == 'T') xDiagonal++;
		if (game[line][line] == 'O' || game[line][line] == 'T') oDiagonal++;
		if (game[line][3 - line] == 'X' || game[line][3 - line] == 'T') xDiagonalInverse++;
		if (game[line][3 - line] == 'O' || game[line][3 - line] == 'T') oDiagonalInverse++;
		for (int index = 0; index < 4; index++) {
			if (game[line][index] == '.') incomplete++;
			if (game[line][index] == 'X' || game[line][index] == 'T') xHorizontal++;
			if (game[line][index] == 'O' || game[line][index] == 'T') oHorizontal++;
			if (game[index][line] == 'X' || game[index][line] == 'T') xVertical++;
			if (game[index][line] == 'O' || game[index][line] == 'T') oVertical++;
		}
		if (xHorizontal == 4 || xVertical == 4) return X;
		if (oHorizontal == 4 || oVertical == 4) return O;
		if (xDiagonal == 4 || xDiagonalInverse == 4) return X;
		if (oDiagonal == 4 || oDiagonalInverse == 4) return O;
		xHorizontal = oHorizontal = xVertical = oVertical = 0;
	}
	
	//if there are missing spaces and no winner the game is incomplete
	if (incomplete) return I;
	
	//if nothing else is correct then it is a draw
	return D;
}
