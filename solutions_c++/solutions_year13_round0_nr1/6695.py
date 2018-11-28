#include<iostream>
#include<fstream>
using namespace std;

ifstream in("in.txt",ios::in);
ofstream out("output.txt",ios::out);
void solve();

void main()
{
	int num;
	in>>num;
	for(int i=1 ; i<=num ; i++)
	{
		out<<"Case #"<<i<<": ";
		solve();
	}
}

bool checkWon(char board[][4], char tocheck)
{
	for(int i=0 ; i<4 ; i++)
	{
		if((board[i][0]==tocheck || board[i][0]=='T') && (board[i][1]==tocheck || board[i][1]=='T') && (board[i][2]==tocheck || board[i][2]=='T') && (board[i][3]==tocheck || board[i][3]=='T'))
			return true;
	}
	for(int i=0 ; i<4 ; i++)
	{
		if((board[0][i]==tocheck || board[0][i]=='T') && (board[1][i]==tocheck || board[1][i]=='T') && (board[2][i]==tocheck || board[2][i]=='T') && (board[3][i]==tocheck || board[3][i]=='T'))
			return true;
	}
	if((board[0][0]==tocheck || board[0][0]=='T') && (board[1][1]==tocheck || board[1][1]=='T') && (board[2][2]==tocheck || board[2][2]=='T') && (board[3][3]==tocheck || board[3][3]=='T'))
			return true;
	if((board[0][3]==tocheck || board[0][3]=='T') && (board[1][2]==tocheck || board[1][2]=='T') && (board[2][1]==tocheck || board[2][1]=='T') && (board[3][0]==tocheck || board[3][0]=='T'))
			return true;
	return false;
}

bool checkIfNotComplete(char board[][4])
{
	for(int i=0 ; i<4 ; i++)
		for(int j=0 ; j<4 ; j++)
			if(board[i][j]=='.')
				return true;
	return false;
}

void solve()
{
	char board[4][4];
	for(int i=0 ; i<4 ; i++)
		for(int j=0 ; j<4 ; j++)
			in>>board[i][j];
	if(checkWon(board,'X'))
	{
		out<<"X won\n";
	}
	else if(checkWon(board,'O'))
	{
		out<<"O won\n";
	}
	else if(checkIfNotComplete(board))
	{
		out<<"Game has not completed\n";
	}
	else
		out<<"Draw\n";
}