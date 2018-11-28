#include <iostream>
#include <fstream>
#include <string>
#include <time.h>

using namespace std;

#define BOARD_SIZE 16
#define BOARD_HEIGHT 4
#define BOARD_WIDTH 4

typedef enum {
	INCOMPLETE, X_WON, O_WON, DRAW
} Outcome;


int checkWin(char* board) {
	char *ptrOne, *ptrTwo, *boardEnd;
	int xCountOne, oCountOne, xCountTwo, oCountTwo, xCountThree, oCountThree, xCountFour, oCountFour, ctr, ptrTwoStep;
	bool draw;
	
	draw = true;
	ptrOne = board;
	ptrTwo = board;
	ptrTwoStep = 4;
	xCountOne = 0;
	oCountOne= 0;
	xCountTwo = 0;
	oCountTwo = 0;
	xCountThree = 0;
	oCountThree = 0;
	xCountFour = 0;
	oCountFour = 0;
	boardEnd = board + BOARD_SIZE;
	
	//Check rows & colums and diagonals
	ctr = 1;
	while(ptrOne != boardEnd) {
		
		if(*ptrOne == '.')
			draw = false;
		
		//Rows
		if(*ptrOne == 'X' || *ptrOne == 'T')
			++xCountOne;
		if(*ptrOne == 'O' || *ptrOne == 'T')
			++oCountOne;
		
		//Cols
		if(*ptrTwo == 'X' || *ptrTwo == 'T')
			++xCountTwo;
		if(*ptrTwo == 'O' || *ptrTwo == 'T')
			++oCountTwo;
		
		if(xCountOne == 4 || xCountTwo == 4)
			return X_WON;
		if(oCountOne == 4 || oCountTwo == 4)
			return O_WON;

		//diag neg
		if((ctr-1)%5 == 0) {
			if(*ptrOne == 'X' || *ptrOne == 'T')
				++xCountThree;
			if(*ptrOne == 'O' || *ptrOne == 'T')
				++oCountThree;
		}
		
		//diag pos
		if((ctr-1)%3 == 0 && ctr != 1 && ctr != 16) {
			if(*ptrOne == 'X' || *ptrOne == 'T')
				++xCountFour;
			if(*ptrOne == 'O' || *ptrOne == 'T')
				++oCountFour;
		}

		if(ctr%BOARD_WIDTH == 0) {
			xCountOne = 0;
			oCountOne = 0;
			xCountTwo = 0;
			oCountTwo = 0;
			
			++ptrTwo;
			ptrTwoStep *= -1;
		}
		else {
			ptrTwo += ptrTwoStep;
		}
		++ptrOne;
		++ctr;
	}
	if(xCountThree == 4 || xCountFour == 4)
		return X_WON;
	if(oCountThree == 4 || oCountFour == 4)
		return O_WON;
	
	if(draw)
		return DRAW;
	return 0;
}

int main() {
	char board[BOARD_SIZE]; 
	//= {'X', 'X', 'X', 'T', '.', '.', '.', '.', 'O', 'O', '.', '.', '.', '.', '.', '.'};
	
	clock_t one, two;
	
	one = clock();
	string line;
	int numberOfCases = 0, i, j, outcome;
	ifstream inFile ("A-large.in");
	ofstream outFile ("A-large-out.txt");
	
	if (inFile.is_open() && outFile.is_open()) {
		//Getting number of test cases
		getline(inFile,line);
		numberOfCases = atoi(line.c_str());

		for(i = 1; i <= numberOfCases; ++i) {
			for(j = 0; j < BOARD_SIZE; ++j) {
				if(j%BOARD_WIDTH == 0){
					getline(inFile, line);
				}
				board[j] = line.at(j%4);
			}
			getline(inFile, line);
			outcome = checkWin(board);
			outFile << "Case #" << i << ": ";
			switch(outcome) {
				case 0:
					outFile << "Game has not completed";
					break;
				case 1:
					outFile << "X won";
					break;
				case 2:
					outFile << "O won";
					break;
				default:
					outFile << "Draw";
				
			}
			outFile << endl;
		}
		inFile.close();
		outFile.close();
	}
	else cout << "Unable to open file";
	two = clock();
	cout << "Time taken in sec: " << (((double) (two - one)) / CLOCKS_PER_SEC) << endl;

	return 0;
}