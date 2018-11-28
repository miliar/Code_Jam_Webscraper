#include <iostream>
using namespace std;

#define GAME_A_WIN			0
#define GAME_B_WIN			1
#define GAME_DRAW			2
#define GAME_NOT_ENDED		3

typedef struct GAME {
	char board[4][4];
} GAME;

int DistinctGame(struct GAME game);

int main() 
{
	size_t size, i, j, k;
	int* result;
	GAME tmp;

	cin >> size;
	result = new int[size];

	for(i=0; i<size; i++)
	{
		for(j=0; j<4; j++)
		{
			for(k=0; k<4; k++)
			{
				cin >> tmp.board[j][k];
			}
		}

		result[i] = DistinctGame(tmp);
	}

	for(i=0; i<size; i++)
	{
		cout << "Case #" << i+1 << ": ";
		switch(result[i]) {
		case GAME_A_WIN : cout << "O won" << endl; break;
		case GAME_B_WIN : cout << "X won" << endl; break;
		case GAME_DRAW : cout << "Draw" << endl; break;
		case GAME_NOT_ENDED : cout << "Game has not completed" << endl; break;
		}
	}

	delete[] result;
}

int DistinctGame(struct GAME game)
{
	int i, j;
	int A_num=0, B_num=0, T_num=0;
	char tmp;

	for(i=0; i<4; i++)
	{
		tmp = game.board[i][0];
		if(tmp == 'T') tmp = game.board[i][1];
		if(tmp == '.') continue;

		for(j=0; j<4; j++)
		{
			if(game.board[i][j] == tmp || game.board[i][j] == 'T') continue;
			else break;
		}

		if(j == 4) {
			if(tmp == 'O') return GAME_A_WIN;
			else if(tmp == 'X') return GAME_B_WIN;
		}
	}

	for(i=0; i<4; i++)
	{
		tmp = game.board[0][i];
		if(tmp == 'T') tmp = game.board[1][i];
		if(tmp == '.') continue;

		for(j=0; j<4; j++)
		{
			if(game.board[j][i] == tmp || game.board[j][i] == 'T') continue;
			else break;
		}

		if(j == 4) {
			if(tmp == 'O') return GAME_A_WIN;
			else if(tmp == 'X') return GAME_B_WIN;
		}
	}

	for(int i=0; i<4; i++)
	{
		if(game.board[i][i] == 'O') A_num++;
		else if(game.board[i][i] == 'X') B_num++;
		else if(game.board[i][i] == 'T') T_num++;
		else break;
	}

	if(i == 4) {
		if(A_num == 4 || (A_num == 3 && T_num == 1)) return GAME_A_WIN;
		else if(B_num == 4 || (B_num == 3 && T_num == 1)) return GAME_B_WIN;
	}

	A_num = 0;
	B_num = 0;
	T_num = 0;

	for(int i=0; i<4; i++)
	{
		if(game.board[3-i][i] == 'O') A_num++;
		else if(game.board[3-i][i] == 'X') B_num++;
		else if(game.board[3-i][i] == 'T') T_num++;
		else break;
	}

	if(i == 4) {
		if(A_num == 4 || (A_num == 3 && T_num == 1)) return GAME_A_WIN;
		else if(B_num == 4 || (B_num == 3 && T_num == 1)) return GAME_B_WIN;
	}

	bool HasNoDot = true;

	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
			if(game.board[i][j] == '.') HasNoDot = false;
	}

	if(HasNoDot) return GAME_DRAW;

	return GAME_NOT_ENDED;
}
