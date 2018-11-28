#include<iostream>
#include<fstream>
using namespace std;
/* 
     0 1 2 3
   0
   1
   2
   3

 */
char a[4][4]={0};
ifstream file("input.txt");
int testno=0;

int playgame(char player, char other)
{
	int score;
	for(int i=0;i<4;i++)
	{
		score=0;
		for(int j=0;j<4;j++)
		{
			if((a[i][j]==player) || (score==3 && a[i][j]=='T'))
			{
				score++;
			}
			else
			{
				if(a[i][j] == other)
				{
					score=0;
				}
			}
		}
		if(score == 4)
		{	/*
			cout<<"row case is true "<<player<<endl;*/
			return score;
		}
	}

	for(int i=0;i<4;i++)
	{
		score=0;
		for(int j=0;j<4;j++)
		{
			
			if((a[j][i]==player) || (score==3 && a[j][i]=='T'))
			{
				score++;
			}
			else
			{
				if(a[j][i] == other)
				{
					score=0;
				}
			}
		}
		if(score == 4)
		{
			/*
			cout<<"column case is true "<<player<<endl;*/
			return score;
		}
	}

	score=0;
	for(int i=0;i<4;i++)
	{
		if((a[i][i]==player) || (score == 3 && a[i][i]=='T'))
		{
			score++;
		}
		else
		{
			if(a[i][i] == other)
			{
				score=0;
			}
		}
	
	}
	if(score == 4)
	{/*
		cout<<"diagonal case is true "<<player<<endl;*/
		return score;
	}
	
	score = 0;
	for(int i=0;i<4;i++)
	{
	
		if((a[i][3-i]==player) || (score == 3 && a[i][3-i]=='T'))
		{
			score++;
		}
		else
		{
			if(a[i][3-i] == other)
			{
				score=0;
			}
		}
	}
	if(score == 4)
	{
		/*
		cout<<"reverse diagonal is true "<<player<<endl;*/
		return score;
	}

	return 0;
}


void readgame(int id)
{
	int fills=0;
	int empty=0;
	
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{

			file>>a[i][j];
			if((a[i][j]=='X')|| (a[i][j]=='O') || (a[i][j]=='T') )
				fills++;
			else
				empty++;
		}
	}
	/*
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{

			cout<<a[i][j]<<" ";
		}
		cout<<"\n";
	}
	cout<<endl;
*/
	int X =playgame('X','O');
	int O = playgame('O','X');

	if(id!=0)
	cout<<endl;
	if(X==4)
		cout<<"Case #"<<(id+1)<<": "<<"X won";
	else
	if(O==4)
		cout<<"Case #"<<(id+1)<<": "<<"O won";
	else
	{
		if(empty>0)
			cout<<"Case #"<<(id+1)<<": "<<"Game has not completed";
		else
		{
			if(X==0 && O==0)	
			cout<<"Case #"<<(id+1)<<": "<<"Draw";		
		}
	}


		
/*	
	cout<<"DEBUG INFO"<<endl;
	cout<<"Fills: "<<fills<<endl;
	cout<<"Empty: "<<empty<<endl;
	cout<<"player X: "<<playgame('X','O')<<endl;
	cout<<"player O: "<<playgame('O','X')<<endl;
	cout<<"------"<<endl<<endl<<endl;*/
}

int main()
{
	file>>testno;
	int i;
	for(i=0;i<testno;i++)
	{
		readgame(i);
	}

file.close();



	return 0;
}
