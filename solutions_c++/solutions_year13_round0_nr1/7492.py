#include<iostream>
#include<fstream>
#include<conio.h>
#include<iomanip>
#include<assert.h>
#include<ctype.h>
#include<errno.h>
#include<float.h>
#include<limits.h>
#include<locale.h>
#include<math.h>
#include<string.h>
#include<stdarg.h>
#include<stddef.h>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<wchar.h>
#include<wctype.h>
#include<queue>
#include<vector>
#include<list>
//#include<E:\gcj\header\BigInt\BigInt.h>
//#include<E:\gcj\header\BigInt\BigInt.cpp>
#define bigint CBigInt
#define max(a,b) a>b?a:b
#define min(x,y) x>y?y:x
//#include<E:\gcj\header\ritwik.H>
using namespace std;
int won(char b[4][4],char player)
{
	int i,j;
	int flag;
	for(i=0;i<4;i++)
	{
		flag=0;
		for(j=0;j<4;j++)
		{
			if(!(b[i][j]==player||b[i][j]=='T'))
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
			return 1;
	}
	for(j=0;j<4;j++)
	{
		flag=0;
		for(i=0;i<4;i++)
		{
			if(!(b[i][j]==player||b[i][j]=='T'))
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
			return 1;
	}
	if((b[0][0]==player||b[0][0]=='T')&&(b[1][1]==player||b[1][1]=='T')&&(b[2][2]==player||b[2][2]=='T')&&(b[3][3]==player||b[3][3]=='T'))
		return 1;
	if((b[0][3]==player||b[0][3]=='T')&&(b[1][2]==player||b[1][2]=='T')&&(b[2][1]==player||b[2][1]=='T')&&(b[3][0]==player||b[3][0]=='T'))
		return 1;
	return 0;
}
void main()
{
	int test;
	int n,a,i,j,pos;
	ifstream fin("A-large.in",ios::binary|ios::in);
	ofstream fout("outputAl.out",ios::out);
	fin>>test;
	char board[4][4];
	int c;
	for(int t_c=0;t_c<test;t_c++)
	{
		c=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fin>>board[i][j];
				if(board[i][j]=='.')
					c++;
			}
		}
		if(won(board,'X'))
			{
				fout<<"Case #"<<t_c+1<<": X won"<<endl;
				cout<<"Case #"<<t_c+1<<": X won"<<endl;
		}
		else if(won(board,'O'))
		{
			fout<<"Case #"<<t_c+1<<": O won"<<endl;
			cout<<"Case #"<<t_c+1<<": O won"<<endl;
		}
		else if(c>0)
		{
			fout<<"Case #"<<t_c+1<<": Game has not completed"<<endl;
			cout<<"Case #"<<t_c+1<<": Game has not completed"<<endl;
		}
		else
		{
			fout<<"Case #"<<t_c+1<<": Draw"<<endl;
			cout<<"Case #"<<t_c+1<<": Draw"<<endl;
		}

	}
	//cout<<sizeof(int)<<" "<<sizeof(long int)<<" "<<sizeof(long long int);
	fin.close();
	fout.close();
	getch();
}

