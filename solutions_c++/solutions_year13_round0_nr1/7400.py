
#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstring>

using namespace std;

const int SIZE = 4;


bool checkdiag(char (&board)[SIZE][SIZE], char T){

	return   (board[0][0] == T && board[1][1] == T && board[2][2] == T  && board[3][3] == T ) ||
	        (board[0][3] == T && board[1][2] == T && board[2][1] == T && board[3][0] == T);
}

bool checkhoriz(char (&board)[SIZE][SIZE], char T){

	for(int i = 0; i < SIZE; i++){
		bool r = true;
		for(int j = 0; j < SIZE; j++){
		        r = r && (T == board[i][j]);
		}
		if(r) return true;
	}
	return false;
}

bool checkvert(char (&board)[SIZE][SIZE], char T){

	for(int j = 0; j < SIZE; j++){
		bool r = true;
		for(int i = 0; i < SIZE; i++){
		        r = r && (T == board[i][j]);
		}
		if(r) return true;
	}
	return false;
}

bool solve(char (&board)[SIZE][SIZE], char T){

	return checkdiag(board, T) || checkhoriz(board, T) || checkvert(board, T);
}

void clear(char (&board)[SIZE][SIZE], char R){
	for(int i = 0; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++){
			if(board[i][j] != R ){
				if(board[i][j] == 'T')
					board[i][j] = R;
				else
					board[i][j] = '.';
			}

		}
	}
}


void show(char (&board)[SIZE][SIZE]){

	for(int i = 0; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++){
			cout<<board[i][j];
		}cout<<endl;
	}
	cout<<endl;
}


bool isfull(char (&board)[SIZE][SIZE]){

	for(int i = 0; i < SIZE; i++){
		for(int j = 0; j < SIZE; j++){
			if(board[i][j] == '.')
				return false;
		}
	}
	return true;
}
int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	char boardX[SIZE][SIZE], boardO[SIZE][SIZE];
	string line;
	int T;

	memset(boardX,'.',sizeof(boardX));
	memset(boardO,'.',sizeof(boardO));
	cin>>T;

	int c = 0;
	for(int i = 0; i < T; i++){
		for(int d = 0; d < SIZE; d++){
			cin>>line;
			for(int i = 0; i < line.length(); i++){
				boardX[d][i] = line[i];
				boardO[d][i] = line[i];

			}
		}

		bool full = isfull(boardX);

		clear(boardX,'X');
		clear(boardO,'O');
		//show(boardX);
		//show(boardO);
		bool X =  solve(boardX, 'X');
		bool O =  solve(boardO, 'O');

		//cout<<X<<" "<<O<<" "<<full<<endl;
		cout<<"Case #"<<i+1<<": ";
		if(!X && !O && full){
			cout<<"Draw"<<endl;
		}
		else if(X){
			cout<<"X won"<<endl;
		}
		else if(O){
			cout<<"O won"<<endl;
		}
		else{
			cout<<"Game has not completed"<<endl;
		}

	}

	return 0;
}
