#include <iostream>
#include <fstream>
using namespace std;

const int N = 4;

char board[N][N];

int T;

ifstream input("in.txt");

void read()
{
	for (int i = 0 ; i < N ; ++i)
		for (int j = 0 ; j < N ; ++j)
			input >> board[i][j];
}


void solve()
{	
	//row
	for (int i = 0 ; i < N ; ++i){
		bool win = true;
		char first = board[i][0];
		if (first == '.')
			continue;
//		cout << "first: " << first << endl;
		for (int j = 1 ; j < N ; ++j){
//				cout << "i= " << i << ", j= " << j << ", " << board[i][j] << endl;
			if (board[i][j] != first && board[i][j] != 'T') {
//				cout << "false: " << i << " " << j << endl;
				win = false;
				break;
			}
		}
		if (win){
			cout << first << " won" << endl;
			return;
		}
	}
 

	//column
	for (int j = 0 ; j < N ; ++j){
		bool win = true;
		char first = board[0][j];
		if (first == '.')
			continue;
		for (int i = 1 ; i < N ; ++i)
			if (board[i][j] != first && board[i][j] != 'T'){
				win = false;
				break;
			}
		if (win){
			cout << first << " won" << endl;
			return;
		}
	}

	//diagonal
	char first = board[0][0];
	bool win = true;
	if (first != '.'){
		for (int i = 1 ; i < N ; ++i)
			if (board[i][i] != first && board[i][i] != 'T'){
				win = false;
				break;
			}
	}
	if (win && first != '.'){
		cout << first << " won" << endl;
		return;
	}	


	//anti diagonal
	first = board[0][3];
	win = true;
	if (first != '.'){
		if ((first == board[1][2] || board[1][2] == 'T') &&
		(first == board[2][1] || board[2][1] == 'T') &&
		(first == board[3][0] || board[3][0] == 'T')){ 
			cout << first << " won" << endl;
			return;
		}

	}


	//check full
	bool full = true;
	for (int i = 0 ; i < N ; ++i){
		if (!full)
			break;
		for (int j = 0 ; j < N ; ++j)
			if (board[i][j] == '.'){
				full = false;
				break; 
			}
	}
	
	if (full)
		cout << "Draw" << endl;
	else
		cout << "Game has not completed" << endl;
}



int main()
{
	input >> T;
	for (int i = 0 ; i < T ; ++i){
		read();
		cout << "Case #" << i+1 << ": ";
		solve();
	}	
}
