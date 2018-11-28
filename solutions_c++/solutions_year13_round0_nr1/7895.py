// tictactoetomek.cpp: define el punto de entrada de la aplicación de consola.
//


#include "stdafx.h"
#include "iostream"
using namespace std;
int T,temp,c,temp1;
	char row[4];
	void rown(int,int,int);
	void compare();
	bool GameOver=false;
	int cases[1000];
	char Table[16];
void main(){	
	cin>>T;
	for( c = 0;c<T;c++)
	{		
		temp=0;
		GameOver=false;

		for(int x=0;x<4;x++)
		{
			cin>>row;
			Table[temp]=row[0];
			Table[temp+1]=row[1];
			Table[temp+2]=row[2];
			Table[temp+3]=row[3];
			temp=temp+4;
		}
		rown(0,4,1);
		rown(4,8,1);
		rown(8,12,1);
		rown(12,16,1);
		rown(0,13,4);
		rown(1,14,4);
		rown(2,15,4);
		rown(3,16,4);
		rown(0,16,5);
		rown(3,13,3);
	
		if(GameOver==false)
		{
		for(int x = 0 ; x<16;x++)
		{
			if(Table[x]=='.')
			{
	
			GameOver=true;
			cases[c]=4;
	
			}
		}	
		}
		if(GameOver==false)
		{
			GameOver=true;
			cases[c]=3;
		}
	}
	for(int x = 0;x<T;x++)
	{
	if(cases[x]==1)
	{cout<<"Case #"<<x+1<<": X won\n";}
	
	if(cases[x]==2)
	{cout<<"Case #"<<x+1<<": O won\n";}

	if(cases[x]==3)
	{cout<<"Case #"<<x+1<<": Draw\n";}

	if(cases[x]==4)
	{cout<<"Case #"<<x+1<<": Game has not completed\n";}
	}
	cin.ignore();
	cin.ignore();
	cin.ignore();
}
void rown(int i,int l, int a)
{
	temp=0;
	for(int x = i; x < l ;x=x+a)
	{
	row[temp]=Table[x];
	temp++;
	}
	compare();
}
void compare()
{
	for(int x=0;x<4;x++)
	{
		if(row[x]=='T')
		{
			if(x>0)
				row[x]=row[x-1];
			else
				row[x]=row[x+1];
		}
	}

	if(row[0]==row[1]&&row[0]==row[2]&&row[0]==row[3])
	{

if(row[0]=='X')
	{
		GameOver=true;
		cases[c]=1;
	}
if(row[0]=='O')
	{	GameOver=true;
		cases[c]=2;
	}
	}

}

