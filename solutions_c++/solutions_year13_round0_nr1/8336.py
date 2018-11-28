#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

bool win(char a, char b, char c, char d, char player){
	int sum = (int) a + (int) b + (int) c + (int) d;
	int four = (4 * (int) player);
	int three = (3 * (int) player + 84);
	if(sum == four || sum == three){
		return true;
	} else {
		return false;
	}
}

bool checkDiags(char player, vector<string> board){
	if(win(board[0][0], board[1][1], board[2][2], board[3][3], player)){
		return true; 
	} else if(win(board[0][3], board[1][2], board[2][1], board[3][0], player)){
		return true;
	} else {
		return false;
	}
}

bool checkWin(char player, vector<string> board){
	if(checkDiags(player, board)){
		return true;
	}

	for(int i = 0; i < 4; i++){
		if(win(board[0][i], board[1][i], board[2][i], board[3][i], player)){
			return true; 
		} else if(win(board[i][0], board[i][1], board[i][2], board[i][3], player)){
			return true;
		}	

	}
	return false;
}

int main(){
	string str;
	getline(cin, str);
	int t = atoi(str.c_str());
	bool x, o = false;
	vector <string> board;
	for(int i=0; i<t; i++){
		//for each test case
		board.clear();
		for(int j = 0; j < 4; j++){
			getline(cin, str);
			//add each row
			board.push_back(str); 
		}
		getline(cin,str); //eat newline
		x = checkWin('X', board);
		o = checkWin('O', board);
		cout << "Case #" << i + 1 << ": ";
		if(x && !o) cout << "X won" << endl;
		else if(!x && o) cout << "O won" << endl;
		else if(x && o) cout << "Draw" << endl;
		else if(!x && !o){
			int total = 0;
			for(int k=0; k < 4; k++){
				for(int l=0; l < 4; l++){
					total += board[k][l];	
				}
			}
			if(total >= (79 * 16)){
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;
			}
		}
	}
}
