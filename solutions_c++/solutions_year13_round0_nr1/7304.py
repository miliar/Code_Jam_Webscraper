//James Rottinger
//Code Jam qualier round
//Tic-Tac-Toe-Tomek
//Driver File

#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

void analyzer(char[4][4], ofstream&, int);
bool verticalWin(char Player, char[4][4]);
bool horizontalWin(char Player, char[4][4]);
bool diagonalWin(char Player, char[4][4]);
bool Draw(char[4][4]);

int main (){

	string filename;
	ifstream inputFile;
	ofstream outputFile;
	char gameBoard[4][4];

	cout << "Please enter the name of the input file with extension\n" ;
	cin >> filename;

	inputFile.open(filename.c_str());
	outputFile.open("output.txt");

	char boardspace;
	int numCases, casesTested=0;

	inputFile >> numCases;

	cout << "There are " << numCases << " cases.\n" << endl;

	int charCounter=0, lineCounter=0;

	while (inputFile >> boardspace){
		gameBoard[charCounter][lineCounter] = boardspace;
		charCounter++;

		if (charCounter==4){
			charCounter=0;
			lineCounter++;
		}

		if (lineCounter==4){
			lineCounter=0;
			analyzer(gameBoard, outputFile, casesTested);
			casesTested++;
		}
	} 
}

void analyzer(char gameBoard[4][4], ofstream& outputFile, int caseNum){
	if (verticalWin('X', gameBoard) || horizontalWin('X', gameBoard) || diagonalWin('X', gameBoard))
		outputFile << "Case #" << caseNum + 1 << ": X won" << endl;
	else if (verticalWin('O', gameBoard) || horizontalWin('O', gameBoard) || diagonalWin('O', gameBoard))
		outputFile << "Case #" << caseNum + 1 << ": O won" << endl;
	else{
		if (Draw(gameBoard))
			outputFile << "Case #" << caseNum + 1 << ": Draw" << endl;
		else
			outputFile << "Case #" << caseNum + 1 << ": Game has not completed" << endl;
	}
}

bool verticalWin(char Player, char gameBoard[4][4]){
	bool result;
	for (int column=0; column < 4; column++){
		if ((gameBoard[column][0] == Player || gameBoard[column][0] == 'T') &&
			(gameBoard[column][1] == Player || gameBoard[column][1] == 'T') &&
			(gameBoard[column][2] == Player || gameBoard[column][2] == 'T') &&
			(gameBoard[column][3] == Player || gameBoard[column][3] == 'T')){
				result = true;
				break;
			}
		else
			result = false;
	}

	return result;
}

bool horizontalWin(char Player, char gameBoard[4][4]){
	bool result;
	for (int row=0; row < 4; row++){
		if ((gameBoard[0][row] == Player || gameBoard[0][row] == 'T') &&
			(gameBoard[1][row] == Player || gameBoard[1][row] == 'T') &&
			(gameBoard[2][row] == Player || gameBoard[2][row] == 'T') &&
			(gameBoard[3][row] == Player || gameBoard[3][row] == 'T')){
				result = true;
				break;
			}
		else
			result = false;
	}

	return result;
}

bool diagonalWin(char Player, char gameBoard[4][4]){
	bool result;
	if ((gameBoard[0][0] == Player || gameBoard[0][0] == 'T') &&
		(gameBoard[1][1] == Player || gameBoard[1][1] == 'T') &&
		(gameBoard[2][2] == Player || gameBoard[2][2] == 'T') &&
		(gameBoard[3][3] == Player || gameBoard[3][3] == 'T')){
		result = true;
	}
	else if ((gameBoard[3][0] == Player || gameBoard[3][0] == 'T') &&
			(gameBoard[2][1] == Player || gameBoard[2][1] == 'T') &&
			(gameBoard[1][2] == Player || gameBoard[1][2] == 'T') &&
			(gameBoard[0][3] == Player || gameBoard[0][3] == 'T')){
		result = true;
	}
	else{
		result =false;
	}
	return result;
}

bool Draw(char gameBoard[4][4]){
	bool result=true;
	for (int column=0; column < 4; column++){
		for (int row=0; row < 4; row++){
			if (gameBoard[column][row]=='.'){
				result =false;
			}
		}
	}
	return result;
}