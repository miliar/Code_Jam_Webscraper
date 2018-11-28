#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int T;
char matrix[4][4];
bool xWon=false;
bool oWon=false;
bool draw=false;
bool notCompleted=false;
void winner_control(int sum);
void find_winner(int x);
void showWinner(int i);

ifstream myStream;
ofstream outfile;
int main()
{
	outfile.open("A-large_output.in");
	myStream.open("A-large.in");
	
	if(myStream.is_open())
	{
		myStream >> T ;

		for(int i=1;i<=T;i++)
		{
			
			
			for(int j=0;j<4;j++)
			{	
				for(int k=0;k<4;k++)
				{
					myStream >> matrix[j][k] ;
				}
			}
			find_winner(i);

		}
	}

	return 0;
}

void winner_control(int sum)
{
	if(sum==316 || sum==321)
		{
			oWon=true;
		}
		else if(sum==352 || sum==348)
		{
			xWon=true;
		}
}

void find_winner(int x)
{
	int sum;
	for(int i=0;i<4;i++)
	{
		sum=0;
		for(int j=0;j<4;j++)
		{
			sum+=(int)matrix[i][j];
		}
		winner_control(sum);
	}

	for(int i=0;i<4;i++)
	{
		sum=0;
		for(int j=0;j<4;j++)
		{
			sum+=(int)matrix[j][i];
		}
		winner_control(sum);
	}
	sum=0;
	for(int i=0;i<4;i++)
	{
		sum+=(int)matrix[i][i];
	}
	winner_control(sum);

	sum=0;
	for(int i=0;i<4;i++)
	{
		sum+=(int)matrix[i][3-i];
	}
	winner_control(sum);

	if(xWon==false && oWon==false)
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(matrix[i][j]=='.')
				{
					notCompleted=true;
					break;
				}
			}
			if(notCompleted==true)
			{
				break;
			}
		}
		if(notCompleted==false)
		{
			draw=true;
		}
	}
	showWinner(x);
}

void showWinner(int i)
{
	if(oWon==true)
	{
		outfile<<"Case #"<<i<<": "<<"O won"<<endl;
	}
	else if(xWon==true)
	{
		outfile<<"Case #"<<i<<": "<<"X won"<<endl;
	}
	else if(draw==true)
	{
		outfile<<"Case #"<<i<<": "<<"Draw"<<endl;
	}
	else if(notCompleted==true)
	{
		outfile<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
	}
	else
	{
		outfile<<"Case #"<<i<<": "<<"Error"<<endl;
	}
	
	
	xWon=false;
	oWon=false;
	draw=false;
	notCompleted=false;
}

