#include<iostream>
#include<fstream>
using namespace std;
	
	
class Game{
public:
int testCases,row,col,count,dotsLeft;
char T[4][4],t;
bool gameOver;


void read(ifstream& in,ofstream& out)
{	in>>testCases;
	for(int i=1;i<=testCases;i++)
	{	
		
	
		gameOver=false;
		dotsLeft=0;
		this->chkgame(in);
		if(gameOver && this->t!='.')
		{
		 out<<"Case #"<<i<<": "<<this->t<<" won"<<endl;
		}
		else if(dotsLeft<=1)
		{
		out<<"Case #"<<i<<": Draw"<<endl;
		}
		else{
		out<<"Case #"<<i<<": Game has not completed"<<endl;
		}}}

void chkgame(ifstream& in)
{
	for(int i=0;i<4;i++)
	{
	 for(int j=0;j<4;j++)
	 {
		 in>>T[i][j];
		if(!(T[i][j]=='X'||T[i][j]=='O'||T[i][j]=='T'))
		 {
		 dotsLeft++;
		 }
	 }
	}
	
	row=0;col=0;
	
	for(;row<4 &&gameOver==false;row++)
	{count=0;
		chkrow();
	}

	for(;col<4 &&gameOver==false;col++)
	{   count=0;
		chkcol();
	}
	
	
	if(!gameOver)
	{  diagonal();	}

	if(!gameOver)
	{  
		diagonal2();
	}
	
}

void chkcol()
{
	this->t=T[0][col];
	for(int j=1;j<4;j++)
		{
			if(T[j][col]==this->t||T[j][col]=='T')
			{
			count++;
			}
		}
	if(count==3)
		gameOver=true;
}
void chkrow()
{
	this->t=T[row][0];
	for(int j=1;j<4;j++)
		{
			if(T[row][j]==this->t||T[row][j]=='T')
			{
			count++;
			}
		}
	if(count==3)
		gameOver=true;
}
void diagonal()
{
	count=0;
	t=T[0][0];
		for(int j=1;j<4;j++)
		{
			if(T[j][j]==this->t||T[j][j]=='T')
			{
			count++;
			}
		}
	if(count==3)
		gameOver=true;

}
void diagonal2()
{
		count=0;
		this->t=T[0][3];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(i+j==3)
				{
					if(T[i][j]==this->t||T[i][j]=='T')
					{
					count++;
					}
				}
			}
	if(count==4)
		gameOver=true;
}
};

int main()
{
	ifstream in;
	ofstream out;
	Game chk;
	in.open("input.in",ios::binary);
	out.open("output.in",ios::out);

	chk.read(in,out);

system("pause");
return 0;
}