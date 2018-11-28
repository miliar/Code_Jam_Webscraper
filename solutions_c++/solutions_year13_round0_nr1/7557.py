// POINT.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>

using namespace std;

ifstream fin;
ofstream fout;

const int O = 0;
const int X = 1;
const int T = 2;
const int P = 3;

int s[4][4];
int check(int t)
{
	int i,j;
	bool WIN=false;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(s[i][j]!=t && s[i][j]!=T)
			{
				break;
			}
		}
		if(j>=4)
		{
			WIN=true;
			break;
		}
	}
	
	if(i>=4)
	{
		for(j=0;j<4;j++)
		{
			for(i=0;i<4;i++)
			{
				if(s[i][j]!=t && s[i][j]!=T)
				{
					break;
				}
			}
			if(i>=4)
			{
				WIN=true;
				break;
			}
		}

		if(j>=4)
		{
			for(i=0;i<4;i++)
			{
				if(s[i][i]!=t && s[i][i]!=T)
				{
					break;
				}
			}
			if(i>=4)
			{
				WIN=true;
			}
			else
			{
				for(i=0;i<4;i++)
				{
					if(s[i][3-i]!=t && s[i][3-i]!=T)
					{
						break;
					}
				}
				if(i>=4)
				{
					WIN=true;
				}
			}
		}
	}

	return WIN;
}

int process(int cases)
{

	int i,j;
	char ch;
	bool tmp1,tmp2;

	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fin>>ch;
			if(ch=='O')
			{
				s[i][j]=O;
			}
			if(ch=='T')
			{
				s[i][j]=T;
			}
			if(ch=='X')
			{
				s[i][j]=X;
			}
			if(ch=='.')
			{
				s[i][j]=P;
			}
		}
	}

	tmp1=tmp2=false;

	tmp1=check(X);
	tmp2=check(O);

	fout<<"Case #"<<cases<<": ";
	if(tmp1==true && tmp2==true || tmp1==true && tmp2==false)
	{
		fout <<"X won";
	}
	if(tmp1==false && tmp2==true)
	{
		fout <<"O won";
	}
	if(tmp1==false && tmp2==false)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(s[i][j]==P)
				{
					break;
				}
			}
			if(j<4)
			{
				break;
			}
		}
		if(i<4)
		{
			fout <<"Game has not completed";
		}
		else
		{
			fout <<"Draw";
		}
	}
	fout<<endl;
	return 0;
}

int main()
{
	int k,i;

	fin.open("tmp.in");
	fout.open("tmp.out");
	fin>>k;
	for(i=0;i<k;i++)
	{
		process(i+1);
	}
	fin.close();
	fout.close();
	return 0;
}

