#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> ChangeTo(vector<string> board, char c)
{
	vector<string> res;
	for (int i=0; i<board.size(); i++)
	{
		string s = board[i];
		for (int j=0; j<s.length(); j++)
		{
			if (s[j] == 'T')
				s[j] = c;
		}
		res.push_back(s);
	}
	return res;
}

bool CanWin(vector<string> board, char p)
{
	//horizontal
	for (int i=0; i<board.size(); i++)
	{
		string s = board[i];
		bool eq = true;
		for (int j=0; j<s.length(); j++)
		{
			if (s[j] != p)
				eq = false;
		}
		if (eq)
			return true;
	}
	
	//vertical
	for (int i=0; i<4; i++)
	{
		bool eq = true;
		for (int j=0; j<4; j++)
		{
			if (board[j][i] != p)
				eq = false;
		}
		if (eq)
			return true;
	}

	//diagonal
	bool eq1 = true;
	bool eq2 = true;
	for (int i=0; i<4; i++)
	{
		if (board[i][i] != p)
			eq1 = false;
		if (board[i][3-i] != p)
			eq2 = false;
	}
	if (eq1 || eq2)
		return true;

	return false;
}

//-1 - O won
//0 - Draw
//1 - X won
//2 - Game has not completed
int CheckState(vector<string> board)
{
	vector<string> changedToX = ChangeTo(board, 'X');
	if (CanWin(changedToX, 'X'))
		return 1;
	vector<string> changedToO = ChangeTo(board, 'O');
	if (CanWin(changedToO, 'O'))
		return -1;

	bool end = true;
	for (int i=0; i<board.size(); i++)
	{
		for (int j=0; j<board[i].length(); j++)
		{
			if (board[i][j] == '.')
				end = false;
		}
	}
	if (end)
		return 0;

	return 2;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		vector<string> board;
		string s;
		for (int i=0; i<4; i++)
		{
			cin >> s;
			board.push_back(s);
		}
		int res = CheckState(board);
		printf("Case #%d: ", t);
		if (res == -1)
			printf("O won\n");
		if (res == 0)
			printf("Draw\n");
		if (res == 1)
			printf("X won\n");
		if (res == 2)
			printf("Game has not completed\n");
	}
	return 0;
}