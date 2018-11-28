/*
ID: anubhav6
PROG: packrec
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
#include <vector>
using namespace std;
#define X 1
#define O 0
ifstream fin ("A-small-attempt0.in");
ofstream fout ("A-small-attempt0.out");
void check(int T,vector<vector<char> > board)
{
	int XorO=0;
	
	int rowX,rowO,colX,colO,diaO,diaX,doaX,doaO;
	diaO=diaX=doaX=doaO=0;
	bool empty=false;
	for(int j=0;j<4;j++)
	{
		rowX=rowO=colO=colX=0;
		for(int k=0;k<4;k++)
		{
			//check rows
				if(board[j][k]=='X')
					rowX++;
				else if(board[j][k]=='O')
					rowO++;
				else if(board[j][k]=='T')
				{
					rowX++;
					rowO++;
				}
			
			//check columns
				if(board[k][j]=='X')
					colX++;
				else if(board[k][j]=='O')
					colO++;
				if(board[j][k]=='.')
					empty=true;
				else if(board[k][j]=='T')
				{
					colX++;
					colO++;
				}
			//check diagonals	
				if(j==k)
				{
					if(board[j][k]=='X')
					diaX++;
					else if(board[j][k]=='O')
					diaO++;
					else if(board[j][k]=='T')
					{	
						diaX++;
						diaO++;
					}
				}
				if(j+k==3)
				{
					if(board[j][k]=='X')
					doaX++;
					else if(board[j][k]=='O')
					doaO++;
					else if(board[j][k]=='T')
					{	
						doaX++;
						doaO++;
					}
				}
		}
		if(rowX==4 || colX==4 || diaX==4 || doaX==4)
		{
			fout<<"Case #"<<T+1<<": "<<"X won"<<endl;
			return;
		}
		if(rowO==4 || colO==4 || diaO==4 || doaO==4)
		{
			fout<<"Case #"<<T+1<<": "<<"O won"<<endl;
			return;
		}
	}
	if(empty)
		fout<<"Case #"<<T+1<<": "<<"Game has not completed"<<endl;
	else
		fout<<"Case #"<<T+1<<": "<<"Draw"<<endl;
}
int main()
{
	
	int T;
	fin>>T;
	vector<vector<char> > board(4 , vector<char> (4,'O'));

	for(int i=0;i<T;i++)
	{
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fin>>board[j][k];
			}
		}
		check(i,board);
	}
}