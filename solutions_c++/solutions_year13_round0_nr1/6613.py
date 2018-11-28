#include <iostream>
#include <memory.h>
using namespace std;

const int BOARD_MAX = 4;

int T;
char board[BOARD_MAX][BOARD_MAX+1];

bool isWon(char H)
{
	int i, j;
	bool isT = false;
	for(i = 0; i < BOARD_MAX; i++){
		for(j = 0; j < BOARD_MAX; j++){
			if(board[i][j] == 'T') {
				isT = true;
				break;
			}
		}
		if(isT) break;
	}
	int ti = i, tj = j;
	if(isT) board[ti][tj] = H;

	for(int i = 0; i < BOARD_MAX; i++){
		int isLine = 0;
		for(int j = 0; j < BOARD_MAX; j++){
			if(board[i][j] == H) isLine++;
		}
		if(isLine == 4) goto TRUE;
	}

	for(int j = 0; j < BOARD_MAX; j++){
		int isLine = 0;
		for(int i = 0; i < BOARD_MAX; i++){
			if(board[i][j] == H) isLine++;
		}
		if(isLine == 4) goto TRUE;
	}
	int isLine = 0;
	int isLine2 = 0;
	for(int i = 0; i < BOARD_MAX; i++){
		
		if(board[i][i] == H) isLine++;
		if(board[i][BOARD_MAX-i-1] == H) isLine2++;
		
	}
	if(isLine == 4) goto TRUE;
	if(isLine2 == 4) goto TRUE;

FALSE:
	if(isT) board[ti][tj] = 'T';
	return false;

TRUE:
	if(isT) board[ti][tj] = 'T';
	return true;

}

bool isDraw()
{
	for(int i = 0; i < BOARD_MAX; i++)
		for(int j = 0; j < BOARD_MAX; j++)
			if(board[i][j] == '.') return false;
	return true;
}

int main()
{
	cin>>T;
	int num = 1;
	while(T--){
		for(int i = 0; i < BOARD_MAX; i++)
			cin>>board[i];

		cout<<"Case #"<<num++<<": ";
		if(isWon('X'))			cout<<"X won"<<endl;
		else if(isWon('O'))		cout<<"O won"<<endl;
		else if(isDraw())		cout<<"Draw"<<endl;
		else					cout<<"Game has not completed"<<endl;
	}

	return 0;
}