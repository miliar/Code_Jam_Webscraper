#include<iostream>
#include<stdio.h>
#include<fstream>
#include<cstring>
using namespace std;
char b[4][4];
int t,ti,tj;
int check(char c)
{
	for(int i=0;i<4;i++)
	{
		if(b[i][0]==c && b[i][1]==c && b[i][2]==c && b[i][3]==c) return 1;
		if(b[0][i]==c && b[1][i]==c && b[2][i]==c && b[3][i]==c) return 1;
	}
	if(b[0][0]==c && b[1][1]==c && b[2][2]==c && b[3][3]==c) return 1;
	if(b[3][0]==c && b[2][1]==c && b[1][2]==c && b[0][3]==c) return 1;
	
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	{
		if(b[i][j]=='.') return 2;
	}
	return 0;
}
int main()
{
	ifstream in;
	in.open("in.txt");
	ofstream out;
	out.open("out.txt");
	in>>t;
	for(int k=1;k<=t;k++)
	{
		for(int i=0;i<4;i++) 
		for(int j=0;j<4;j++)
		{
			in>>b[i][j];
			if(b[i][j]=='T') {ti=i;tj=j;} 
		}
		b[ti][tj]='O';
		if(check('O')==1)
		{
			out<<"Case #"<<k<<": O won"<<endl;
		}
		else
		{
			b[ti][tj]='X';
			if(check('X')==1)
			{
				out<<"Case #"<<k<<": X won"<<endl;
			}
			else if(check('X')==2)
			{
				out<<"Case #"<<k<<": Game has not completed"<<endl;
			}
			else
			{
				out<<"Case #"<<k<<": Draw"<<endl;
			}
		}
	}
	return 0;
}