#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
bool isXWon(vector <string> board);
bool isOWon(vector <string> board);
bool isGameFinished(vector <string> board);
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int T;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		vector <string> board;
		for (int j = 0;j < 4; j++)
		{
			string temp;
			cin >> temp;
			board.push_back(temp);
		}
		if (isXWon(board))
		{
			cout << "Case #" << i + 1 << ": X won" << endl;
		}
		else if (isOWon(board))
		{
			cout << "Case #" << i + 1 << ": O won" << endl;
		}
		else
		{
			if (isGameFinished(board))
			{
				cout << "Case #" << i + 1 << ": Draw" << endl;
			}
			else
			{
				cout << "Case #" << i + 1 << ": Game has not completed" << endl;
			}
		}
	}
	return 0;
}

bool isXWon(vector <string> board)
{
	for (int i = 0; i < 4; i++)
	{
		int index = board[i].find('T');
		if (index != -1)
		{
			board[i][index] = 'X';
		}
		if (board[i] == "XXXX")
			return true;
	}
	string diagonal1 ="";
	string diagonal2 ="";
	for (int i = 0; i < 4; i++)
	{
		string temp = "";
		temp += board[0][i];
		temp += board[1][i];
		temp += board[2][i];
		temp += board[3][i];
		if (temp == "XXXX")
			return true;
		diagonal1 += board[i][i];
		diagonal2 += board[i][3-i];
	}
	if (diagonal1 == "XXXX" || diagonal2 == "XXXX")
		return true;
	return false;
}
bool isOWon(vector <string> board)
{
	for (int i = 0; i < 4; i++)
	{
		int index = board[i].find('T');
		if (index != -1)
		{
			board[i][index] = 'O';
		}
		if (board[i] == "OOOO")
			return true;
	}
	string diagonal1 ="";
	string diagonal2 ="";
	for (int i = 0; i < 4; i++)
	{
		string temp = "";
		temp += board[0][i];
		temp += board[1][i];
		temp += board[2][i];
		temp += board[3][i];
		if (temp == "OOOO")
			return true;
		diagonal1 += board[i][i];
		diagonal2 += board[i][3-i];
	}
	if (diagonal1 == "OOOO" || diagonal2 == "OOOO")
		return true;
	return false;
}

bool isGameFinished(vector <string> board)
{
	for (int i = 0; i < 4; i++)
	{
		if (board[i].find('.') != -1)
		{
			return false;
		}
	}

	return true;
}