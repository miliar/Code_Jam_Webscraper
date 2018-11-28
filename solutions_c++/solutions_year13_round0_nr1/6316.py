#include <fstream>
#include <iostream>

using namespace std;

char board[4][4];

bool searchH(int count, char c, int x, int y)
{
	if (count == 4)
		return true;
	
	if (x >= 4 || y >= 4 || x < 0 || y < 0)
		return false;	
	
	if(board[x][y] == c || board[x][y] == 'T')
		return searchH(count+1,c,x+1,y);
	
	return false;
}

bool searchV(int count, char c, int x, int y)
{
	if (count == 4)
		return true;
	
	if (x >= 4 || y >= 4 || x < 0 || y < 0)
		return false;	
	
	if(board[x][y] == c || board[x][y] == 'T')
		return searchV(count+1,c,x,y+1);
	
	return false;
}

bool searchD(int count, char c, int x, int y, bool Up)
{
	if (count == 4)
		return true;
	
	if (x >= 4 || y >= 4 || x < 0 || y < 0)
		return false;	
	
	if(board[x][y] == c || board[x][y] == 'T')
		if (Up)
			return searchD(count+1,c,x+1,y+1,Up);
		else
			return searchD(count+1,c,x+1,y-1,Up);
	
	return false;
}

bool isWin(char c)
{
	bool flagH, flagV, flagD;
	
	flagH = searchH(0,c,0,0)||searchH(0,c,0,1)||searchH(0,c,0,2)||searchH(0,c,0,3);
	flagV = searchV(0,c,0,0)||searchV(0,c,1,0)||searchV(0,c,2,0)||searchV(0,c,3,0);
	flagD = searchD(0,c,0,0,true)||searchD(0,c,0,3,false);
	
	return flagH || flagV || flagD;
	
}

int analizeBoard()
{
	int numberX = 0;
	int numberO = 0;
	bool isComplete = true;
	
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{			
			if (board[i][j] == '.')
				isComplete = false;
		}
	}
			
	if (isWin('X'))
		return 1;
		
	if (isWin('O'))
		return 2;
		
	if (isComplete == true)
		return 3;
	return 4;
}

int main()
{
	int test_cases;
	int res;
	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	fin>>test_cases;
	
	for (int i = 1; i <= test_cases; i++)
	{
		for (int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)
			fin>>board[j][k];
		
		res = analizeBoard();
		
		if (res == 1)
			fout<<"Case #"<<i<<": X won"<<endl;
		else if (res == 2)
			fout<<"Case #"<<i<<": O won"<<endl;
		else if (res == 3)
			fout<<"Case #"<<i<<": Draw"<<endl;
		else
			fout<<"Case #"<<i<<": Game has not completed"<<endl;
		
	}
	
	return 0;
}