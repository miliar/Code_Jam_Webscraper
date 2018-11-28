//============================================================================
// Name        : Tomek.cpp
// Author      : James Walter
// Version     : 1
// Description : Google Code Jam Qualifier Problem A. Tic-Tac-Toe-Tomek
//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

class Game
{
	public:
		char eval();
		void setBoard(string inBoard[4]);
		Game();
	private:
		char board[4][4];
		char checkWins(string s);
};

Game::Game(){

}

void Game::setBoard(string rawBoard[]){
	string s;

	for(int i = 0; i < 4; i++){
		s = rawBoard[i];
		for(int j = 0; j < 4; j++){
			board[i][j] = s[j];
		}
	}

}

char Game::eval(){
	string s;
	char result;
	bool incomplete = false;

	for(int i = 0; i < 4; i++){
		//row
	    s = board[i][0];
	    s += board[i][1];
	    s += board[i][2];
	    s += board[i][3];

	    result = checkWins(s);
	    if(result == 'X' || result == 'O'){
	    	return result;
	    }
	    else if(result == 'I'){
	    	incomplete = true;
	    }
		//column
	    s = board[0][i];
	    s += board[1][i];
	    s += board[2][i];
	    s += board[3][i];
	    result = checkWins(s);
	    if(result == 'X' || result == 'O'){
	   	    	return result;
	   	}
	   	else if(result == 'I'){
	   	    	incomplete = true;
	   	}
	}
	//diag 1
	s = board[0][0];
	s += board[1][1];
	s += board[2][2];
	s += board[3][3];
	result = checkWins(s);
    if(result == 'X' || result == 'O'){
    	return result;
	}
	else if(result == 'I'){
		incomplete = true;
	}

	//diag 2
    s = board[0][3];
    s += board[1][2];
    s += board[2][1];
    s += board[3][0];
	result = checkWins(s);
	if(result == 'X' || result == 'O'){
		return result;
	}
	else if(result == 'I'){
		incomplete = true;
	}

    if(incomplete){
    	return 'I';
    }
    else{
    	return 'D';
    }

}

char Game::checkWins(string s){
	bool i = false;
	bool x = false;
	bool o = false;
	unsigned found;

	found = s.find_first_of('X');
	if (found != std::string::npos) {
		x = true;
	}
	found = s.find_first_of('.');
		if (found != std::string::npos) {
			i = true;
		}
	found = s.find_first_of('O');
		if (found != std::string::npos) {
			o = true;
		}

   if(i){
	   return 'I';
   }
   else if(x && o){
	   return 'D';
   }
   else if(x && !o){
	   return 'X';
   }
   else{
	   return 'O';
   }

}



int main() {
	ofstream outFile;
	ifstream inFile;
	string line;
	string board[4];
	Game g;
	int numCases;
	char result;
	string output;
	int caseNo;


	inFile.open("inTest.txt");
	outFile.open("out.txt");
	getline(inFile, line);
	numCases = atoi(line.c_str());


	for(int i = 0; i < numCases; i++){
		caseNo = i + 1;
		getline(inFile,line);
		board[0] = line;
	    getline(inFile,line);
		board[1] = line;
		getline(inFile,line);
		board[2] = line;
		getline(inFile,line);
		board[3] = line;
		getline(inFile,line);

		g.setBoard(board);
		result = g.eval();
		outFile << "Case #" << caseNo << ": ";
		switch (result) {
			case 'X':
				outFile <<  "X won" << endl;
				break;
			case 'O':
				outFile <<  "O won" << endl;
				break;
			case 'I':
				outFile << "Game has not completed" << endl;
				break;
			case 'D':
				outFile << "Draw" << endl;
				break;
			default:
				break;
		}
	}
	return 0;
}




