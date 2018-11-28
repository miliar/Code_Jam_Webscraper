#include <iostream>
#include <string>
#include<fstream>

using namespace std;
#define SIZE 4 

int main()
{
	int iterate;
	string *boards	= new string [SIZE];
	char won		= '.';
	char prevChar	= '-';
	bool flag		= true;
	bool draw		= true;
	ifstream a("a.txt");
	ofstream myfile;
	myfile.open ("out.txt");


	a>> iterate;
	a.get();
	string *out		= new string [iterate];
	for(int b = 0 ; b<iterate ; b++)
	{
		
 		for(int i=0;i<SIZE;i++)
		{
			a>>boards[i];
			a.get();
		}

		for(int i = 0 ; i<SIZE ; i++)
		{
			for(int j = 0 ; j<SIZE ; j++)
			{
				if(boards[i][j] == 'T')
					continue;
				if(j == 0 || prevChar == '-')
				{
					prevChar = boards[i][j];
					continue;
				}
				if(boards[i][j] == prevChar)
				{
					flag = true;
					prevChar = boards[i][j];
				}
				else
				{
					flag=false;
					break;
				}
			}
			if(flag == true )
				if( prevChar == '.')
				{
					flag = false;
				}
				else
				{
					break;
				}
		}

		if(flag == false)
		{
			prevChar = '-';
			for (int i = 0 ; i< SIZE ; i++)
			{	
				for(int j = 0 ; j<SIZE ; j++)
				{
					if(boards[j][i] == 'T')
						continue;
					if(j == 0 || prevChar == '-')
					{
						prevChar = boards[j][i];
						continue;
					}
					if(boards[j][i] == prevChar)
					{
						flag = true;
						prevChar = boards[j][i];
					}
					else
					{
						flag=false;
						break;
					}
				}
				if(flag == true )	
					if( prevChar == '.')
					{
						flag = false;
					}
					else
					{
						break;
					}		
			}
		}

		if(flag == false)
		{
			prevChar = '-';
			for(int i = 0; i<SIZE ; i++)
			{
				if(boards[i][i] == 'T')
					continue;
				if(i == 0 || prevChar == '-')
				{
					prevChar = boards[i][i];
					continue;
				}
				if(boards[i][i] == prevChar)
				{
					flag = true;
					prevChar = boards[i][i];
				}
				else
				{
					flag=false;
					break;
				}
			}
			if(flag == true )
				if( prevChar == '.')
				{
					flag = false;
				}
		}

		if(flag == false)
		{
			prevChar = '-';

			for(int i = 0; i<SIZE ; i++)
			{	
				if(boards[i][SIZE-i-1] == 'T')		
					continue;
				if(i == 0 || prevChar == '-')
				{
					prevChar = boards[i][SIZE-i-1];
					continue;
				}
				if(boards[i][SIZE-1-i] == prevChar)
				{
					flag = true;
					prevChar = boards[i][SIZE-1-i];
				}
				else
				{
					flag=false;
					break;	
				}
			}
			if(flag == true )
				if( prevChar == '.')
				{
					flag = false;
				}
		}

		if(flag == true)
			won = prevChar;
		else
			for (int i = 0 ; i <SIZE ; i++)
				for(int j = 0 ; j<SIZE ; j++)
					if(boards[i][j]=='.')
						draw=false;

		if(flag == false && draw == true)

			out[b] = "Draw";
		else if (won == 'X')
			out[b]="X won";
		else if (won == 'O')
			out[b]="O won";
		else 
			out[b] = "Game has not completed";
		
		draw = true;
		won = '.';
		}
		cout<<endl;
		for(int i = 0 ; i<iterate ; i++)
			myfile<<"Case #"<< i+1 <<": "<<out[i]<<endl;
	
		myfile.close();	
		system("pause");
	return 0;
}