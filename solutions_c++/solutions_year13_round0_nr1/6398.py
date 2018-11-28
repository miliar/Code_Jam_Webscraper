#include<iostream>
#include<fstream>
using namespace std;

int countVertical(char **board, int i, int j, char player, int size){
	int score = 0;
	int currRow = i;
	
	if(board[i][j] == player || board[i][j] == 'T'){
		++score;
		++currRow;
	
		// Count consecs towards the down
		while(currRow < size){
			if(board[currRow][j] == player || board[currRow][j] == 'T'){
				++score;
				++currRow;
			}
			else
				break;
		}
	
		// Count consecs towards the up
		currRow = i-1;
	
		while(currRow >= 0){
			if(board[currRow][j] == player || board[currRow][j] == 'T'){
				++score;
				--currRow;
			}
			else
				break;
			
		}
	}
	return score;
}	

int countHorizontal(char **board, int i, int j, char player, int size){
	int score = 0;
	int currCol = j;
	
	if(board[i][j] == player || board[i][j] == 'T'){
		++score;
		++currCol;
	
		// Count consecs towards the right
		while(currCol < size){
			if(board[i][currCol] == player || board[i][currCol] == 'T'){
				++score;
				++currCol;
			}
			else
				break;
			
		}
	
		// Count consecs towards the left
		currCol = j-1;
	
		while(currCol >= 0){
			if(board[i][currCol] == player || board[i][currCol] == 'T'){
				++score;
				--currCol;
			}
			else
				break;
			
		}
	}
	return score;
}

// Left up diag
int countDiagLU(char **board, int i, int j, char player, int size){
	int score = 0;
	int currRow = i;
	int currCol = j;
	
	if(board[i][j] == player || board[i][j] == 'T'){
		++score;
		++currRow;
		++currCol;
	
		// Count consecs towards the right-down
		while(currRow < size && currCol < size){
			if(board[currRow][currCol] == player || board[currRow][currCol] == 'T'){
				++score;
				++currRow;
				++currCol;
			}
			else
				break;
			
		}
	
		// Count consecs towards the left-up
		currRow = i-1;
		currCol = j-1;
	
		while(currRow >= 0 && currCol >= 0){
			if(board[currRow][currCol] == player || board[currRow][currCol] == 'T'){
				++score;
				--currRow;
				--currCol;
			}
			else
				break;
			
		}
	}
	return score;
}

// Right up diag
int countDiagRU(char **board, int i, int j, char player, int size){
	int score = 0;
	int currRow = i;
	int currCol = j;
	
	if(board[i][j] == player || board[i][j] == 'T'){
		++score;
		--currRow;
		++currCol;
	
		// Count consecs towards the right-up
		while(currRow >= 0 && currCol < size){
			if(board[currRow][currCol] == player || board[currRow][currCol] == 'T'){
				++score;
				--currRow;
				++currCol;
			}
			else
				break;
			
		}
	
		// Count consecs towards the left-down
		currRow = i+1;
		currCol = j-1;
	
		while(currRow < size && currCol >= 0){
			if(board[currRow][currCol] == player || board[currRow][currCol] == 'T'){
				++score;
				++currRow;
				--currCol;
			}
			else
				break;
			
		}
	}
	return score;
}

int checkBoard(char **board, char player, int size){
	int vertical = 0, horizontal = 0, diag = 0;
	int tempV, tempH, tempD;
	int highest;

	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			tempV = countVertical(board, i, j, player, size);
			if(tempV > vertical){
				vertical = tempV;
			}
			
			tempH = countHorizontal(board, i, j, player, size);
			if(tempH > horizontal){
				horizontal = tempH;
			}
			
			tempD = countDiagLU(board, i, j, player, size);
			if(tempD > diag){
				diag = tempD;
			}
			
			tempD = countDiagRU(board, i, j, player, size);
			if(tempD > diag){
				diag = tempD;
			}
		}
	}
	highest = vertical;
	
	if(horizontal > highest){
		highest = horizontal;
	}
	
	if(diag > highest){
		highest = diag;
	}
	return highest;
}

int main(){
	char **board;
	int boardSize = 4;
	int player1Score = 0;
	int player2Score = 0;
	int periods;
	int testCases;
	int currRow, currCol;
	ifstream inFile("in.txt");
	ofstream outFile("out.txt");
	
	if(inFile.is_open()){
	
		board = new char*[boardSize];
	
		for(int i = 0; i < boardSize; i++){
			board[i] = new char[boardSize];
		}
		
		inFile >> testCases;
		
		for(int i = 1; i <= testCases; i++){
			currRow = 0;
			periods = 0;
			while(currRow < boardSize){
				currCol = 0;
				while(currCol < boardSize){
					inFile >> board[currRow][currCol];
					if(board[currRow][currCol] == '.'){
						++periods;
					}
					//cout << board[currRow][currCol] << ' ';
					++currCol;
				}
				//cout << endl;
				++currRow;
			}
		
			player1Score = checkBoard(board, 'X', boardSize);
			player2Score = checkBoard(board, 'O', boardSize);
			
			if(player1Score == 4){
				outFile << "Case #" << i << ": X won" << endl;
				//outFile << player1Score << endl;
				//outFile << player2Score << endl;
			}
			else if(player2Score == 4){
				outFile << "Case #" << i << ": O won" << endl;
				//outFile << player1Score << endl;
				//outFile << player2Score << endl;
			}
			else if(periods > 0){
				outFile << "Case #" << i << ": Game has not completed" << endl;
				//outFile << player1Score << endl;
				//outFile << player2Score << endl;
			}
			else{
				outFile << "Case #" << i << ": Draw" << endl;
				//outFile << player1Score << endl;
				//outFile << player2Score << endl;
			}
		}
	}
	
	return 0;
}