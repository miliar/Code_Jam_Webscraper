#include<iostream>
#include<fstream>
using namespace std;
#define X 'X'
#define O 'O'
#define T 'T'
#define DOT '.'
enum
{
	X_won,//(the game is over, and X won)
O_won, //(the game is over, and O won)
Draw ,//(the game is over, and it ended in a draw)
Game_has_not_completed// (the game is not over yet)
};


struct testcase
{
	char board[4][4];
	int trow;
	int tcol;
	int res;
	int numempty;
	testcase()
	{
		numempty=0;
		res=Game_has_not_completed;
		/*for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				board[i][j]=
			}
		}*/
	}
};

void checkrow(testcase &tc)
{
	for(int i=0;i<4;i++)
	{
		int xcount=0;
		int ocount=0;
		for(int j=0;j<4;j++)
		{
			if(tc.board[i][j]==X)
			{
				xcount++;
			}
			else if(tc.board[i][j]==O)
			{
				ocount++;
			}

		}
		if(xcount==4 || (xcount==3&&tc.trow==i))
		{
			tc.res=X_won;
		}
		else if(ocount==4 || (ocount==3 && tc.trow==i))
		{
			tc.res=O_won;
		}
	}
}
void checkcol(testcase &tc)
{
	for(int i=0;i<4;i++)
	{
		int xcount=0;
		int ocount=0;
		for(int j=0;j<4;j++)
		{
			if(tc.board[j][i]=='X')
			{
				xcount++;
			}
			else if(tc.board[j][i]=='O')
			{
				ocount++;
			}
		}
		if(xcount==4 || (xcount==3&&tc.tcol==i))
		{
			tc.res=X_won;
		}
		else if(ocount==4 || (ocount==3 && tc.tcol==i))
		{
			tc.res=O_won;
		}
	}
}
void checkdiag(testcase &tc)
{
	if((tc.board[0][0]=='X'||tc.board[0][0]=='T')&&(tc.board[1][1]=='X'||tc.board[1][1]=='T')&&(tc.board[2][2]=='X'||tc.board[2][2]=='T')&&(tc.board[3][3]=='X'||tc.board[3][3]=='T'))
	{
		tc.res=X_won;

	}
	else if((tc.board[0][0]=='O'||tc.board[0][0]=='T')&&(tc.board[1][1]=='O'||tc.board[1][1]=='T')&&(tc.board[2][2]=='O'||tc.board[2][2]=='T')&&(tc.board[3][3]=='O'||tc.board[3][3]=='T'))
	{
		tc.res=O_won;

	}

	//////// checking other diag//
	if((tc.board[0][3]=='X'||tc.board[0][3]=='T')&&(tc.board[1][2]=='X'||tc.board[1][2]=='T')&&(tc.board[2][1]=='X'||tc.board[2][1]=='T')&&(tc.board[3][0]=='X'||tc.board[3][0]=='T'))
	{
		tc.res=X_won;
	}
	else if((tc.board[0][3]=='O'||tc.board[0][3]=='T')&&(tc.board[1][2]=='O'||tc.board[1][2]=='T')&&(tc.board[2][1]=='O'||tc.board[2][1]=='T')&&(tc.board[3][0]=='O'||tc.board[3][0]=='T'))
	{
		tc.res=O_won;
	}
}
int main()
{

	ifstream inf("inpout.txt");
	ofstream outf("output.txt");
	int numtc=0;
	inf>>numtc;
	testcase * tc = new testcase[numtc]; 
	for(int i=0;i<numtc;i++)
	{
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				inf>>tc[i].board[j][k];
				if(tc[i].board[j][k]=='T')
				{
					tc[i].trow=j;
					tc[i].tcol=k;
				}
				if(tc[i].board[j][k]=='.')
				{
					tc[i].numempty++;
				}
			}
		}
		//char ch;
		//inf>>ch;
	}

	//////////////////////////////

	for(int i=0;i<numtc;i++)
	{
		checkrow(tc[i]);
		checkcol(tc[i]);
		checkdiag(tc[i]);
		if(tc[i].res==X_won)
		{
			outf<<"Case #"<<i+1<<": X won"<<endl;
			continue;
		}
		else if(tc[i].res==O_won)
		{
			outf<<"Case #"<<i+1<<": O won"<<endl;
			continue;
		}
		else if(tc[i].numempty>0)
		{
			outf<<"Case #"<<i+1<<": Game has not completed"<<endl;
			continue;
		}
		else
		{
			outf<<"Case #"<<i+1<<": Draw"<<endl;
			continue;
		}

	}
	return 0;
}

