// tic-tac-toe.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-small-attempt.out");
int tic_tac_toe(char a[4][4]);
char a[4][4];
int main()
{
	int i,j;
	int count=0;
	int count1=0;
	int k=0;
	int cases;
	fin>>cases;
	while(k<cases)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fin>>a[i][j];
				
			}
		}
		fout<<"Case #";
		fout<<k+1;
		fout<<": ";
		int res=tic_tac_toe(a);
		
		switch(res)
		{
			case 1 : fout<<"X won";
					 break;
			case 2 : fout<<"O won";
					 break;
			case 3 : fout<<"Game has not completed";
					 break;
			case 4 : fout<<"Draw";
		}
		fout<<"\n";
		k++;
	}
	return 0;
}
int tic_tac_toe(char a[4][4])
{
	int i,j,count=0;
	//code for checking row wise for X
	for(i=0;i<4;i++)
	{
		count=0;
		for(j=0;j<4;j++)
		{
			if(a[i][j]=='X'||a[i][j]=='T')
				count++;
		}
		if(count==4)
			return(1);
	}
	//code for checkinf col wise for X
	for(i=0;i<4;i++)
	{
		count=0;
		for(j=0;j<4;j++)
		{
			if(a[j][i]=='X'||a[j][i]=='T')
				count++;
		}
		if(count==4)
			return(1);
    }
	count=0;
	//checking right diagonal for x
	for(i=0;i<4;i++)
		if(a[i][i]=='X' || a[i][i]=='T')
	      count++;
	if(count==4)
		return(1);
	//checking left diagonal for x
	if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
		return(1);

	//code for checking row wise for O
	for(i=0;i<4;i++)
	{
		count=0;
		for(j=0;j<4;j++)
		{
			if(a[i][j]=='O'||a[i][j]=='T')
				count++;
		}
		if(count==4)
			return(2);
	}
	//code for checkinf col wise for o
	for(i=0;i<4;i++)
	{
		count=0;
		for(j=0;j<4;j++)
		{
			if(a[j][i]=='O'||a[j][i]=='T')
				count++;
		}
		if(count==4)
			return(2);
    }
	count=0;
	//checking right diagonal for O
	for(i=0;i<4;i++)
		if(a[i][i]=='O' || a[i][i]=='T')
	      count++;
	if(count==4)
		return(2);
	//checking left diagonal for O
	if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
		return(2);

	//check for game end
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(a[i][j]=='.')
				return(3);
	return(4);
}
	


