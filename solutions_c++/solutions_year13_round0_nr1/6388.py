#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

int getStatus(char** board){

	for(int ctrRow = 0; ctrRow<4; ctrRow++){
		int numX = 0;
		int numO = 0;
		for(int ctrCol = 0; ctrCol<4; ctrCol++){
			if(board[ctrRow][ctrCol] == 'X'){
				numX++;
			}
			if(board[ctrRow][ctrCol] == 'O'){
				numO++;
			}
			if(board[ctrRow][ctrCol] == 'T'){
				numX++;
				numO++;
			}
		}

		if(numX == 4){
			return 1;
		}
		if(numO == 4){
			return 2;
		}
	}	
	for(int ctrCol = 0; ctrCol<4; ctrCol++){
		int numX = 0;
		int numO = 0;
		for(int ctrRow = 0; ctrRow<4; ctrRow++){
			if(board[ctrRow][ctrCol] == 'X'){
				numX++;
			}
			if(board[ctrRow][ctrCol] == 'O'){
				numO++;
			}
			if(board[ctrRow][ctrCol] == 'T'){
				numX++;
				numO++;
			}
		}

		if(numX == 4){
			return 1;
		}
		if(numO == 4){
			return 2;
		}
	}

	//Check diagonals
		int numX = 0;
		int numO = 0;
	for(int ctrPos = 0; ctrPos<4; ctrPos++){
			if(board[ctrPos][ctrPos] == 'X'){
				numX++;
			}
			if(board[ctrPos][ctrPos] == 'O'){
				numO++;
			}
			if(board[ctrPos][ctrPos] == 'T'){
				numX++;
				numO++;
			}

		if(numX == 4){
			return 1;
		}
		if(numO == 4){
			return 2;
		}
	}
		numX = 0;
		numO = 0;
	for(int ctrPos = 0; ctrPos<4; ctrPos++){
			if(board[ctrPos][3-ctrPos] == 'X'){
				numX++;
			}
			if(board[ctrPos][3-ctrPos] == 'O'){
				numO++;
			}
			if(board[ctrPos][3-ctrPos] == 'T'){
				numX++;
				numO++;
			}

		if(numX == 4){
			return 1;
		}
		if(numO == 4){
			return 2;
		}
	}

	//Check if game is still going
	int numDots=0;
	for(int ctrCol=0; ctrCol<4; ctrCol++){
		for(int ctrRow=0; ctrRow<4; ctrRow++){
			if(board[ctrRow][ctrCol] == '.'){
				numDots++;
			}
		}
	}
	if(numDots > 0){
		return 4;
	}
	return 3;


}

int main(){
	int testcases;

	std::cin >> testcases;
	getchar();

	for(int ctrCase = 0; ctrCase < testcases; ctrCase++){
		char * board[4];
		for(int ctrRow = 0; ctrRow < 4; ctrRow++){
			char* row = new char[4];
			for(int ctrCol = 0; ctrCol < 4; ctrCol++){
				row[ctrCol] = getchar();
			}
			board[ctrRow] = row;

			getchar();
//			std::cout << board[ctrRow][0] << std::endl;
		}
		getchar();

		int status = getStatus(board);

		switch (status){
			case 1:
				std::cout << "Case #" << ctrCase+1 << ": " << "X won" << std::endl;
				break;
			case 2:
				std::cout << "Case #" << ctrCase+1 << ": " << "O won" << std::endl;
				break;
			case 3:
				std::cout << "Case #" << ctrCase+1 << ": " << "Draw" << std::endl;
				break;
			case 4:
				std::cout << "Case #" << ctrCase+1 << ": " << "Game has not completed" << std::endl;
				break;
		}

		//Cleanup
		for(int ctrRow=0; ctrRow < 4; ctrRow++){
			delete[] board[ctrRow];
		}
	}

}
