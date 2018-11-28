#include <cmath>
#include <iostream>
#include <string>
using namespace std;

const int LEN = 4;
const char PLAYER_X = 'X';
const char PLAYER_O = 'O';
const char DOT = '.';
const char MrT = 'T';
char **board;

void createBoard()
{
	board = new char*[LEN];
	for (int i = 0; i < LEN; ++i)
		board[i] = new char [LEN];
}

void releaseTheBoard()
{
	for(int i = 0 ; i < LEN; i++) 
	{
		delete board[i];

	}
	delete board;

}

int readBoard()
{
	int numberOfDots = 0;
	for(int i = 0 ; i < LEN ; i++)
	{
		for(int j = 0 ; j < LEN ; j++)
		{
			cin >> board[i][j];

			if(board[i][j] == DOT)
				numberOfDots++;
		}
	}	

	return numberOfDots;
}

void showBoard(){
	for(int i = 0 ; i < LEN ; i++)
	{
		for(int j = 0 ; j < LEN ; j++)
		{
			cout << board[i][j];


		}
		cout<<endl;
	}
	cout<<endl;

}


#define LARGE
void setInputOutputStreams()
{
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif

#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
}

bool sameValueInRow(char val, int row){
	for(int i = 0; i < LEN ; i++)
	{
		if(board[i][row] != val && board[i][row] != MrT)
			return false;
	}

	return true;
}


bool sameValueInColumn(char val, int column){
	for(int i = 0; i < LEN ; i++)
	{
		if(board[column][i] != val && board[column][i] != MrT)
			return false;
	}

	return true;
}



bool sameValueDiagonal(char player){

	bool diagonal = true;
	bool inverseDiagonal = true;
	for(int i = 0 ; i < LEN ; i++)
	{
		inverseDiagonal &= (board[LEN - i - 1][i] == player || board[LEN - i - 1][i] == MrT);
		diagonal &= (board[i][i] == player || board[i][i] == MrT);
	}

	return diagonal || inverseDiagonal;
}

bool isPlayerWon(char player)
{
	bool won = false;
	for(int i = 0 ; i < LEN ; i++){
		won |= sameValueInRow(player,i);
		won |= sameValueInColumn(player,i);
	}

	won |= sameValueDiagonal(player);

	return won;
}



int main(int argc, char* argv[])
{
	setInputOutputStreams();
	createBoard();

	int T = 0;	
	int numberOfDots = 0;
	
	cin >> T;

	for(int t = 0 ; t < T ; t++)
	{
		numberOfDots = readBoard();

		cout << "Case #"<<t+1<<": " ;

		if(isPlayerWon(PLAYER_O)){
			cout<<"O won"<<endl;
		}else if(isPlayerWon(PLAYER_X)){
			cout<<"X won"<<endl;
		}else if(numberOfDots ==0 ){
			cout<<"Draw"<<endl;
		}else {
			cout<<"Game has not completed"<<endl;
		}

	}	

	releaseTheBoard();
	return 0;
}

