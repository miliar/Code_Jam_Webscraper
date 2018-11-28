#include <fstream>
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string.h>
using namespace std ;
int main()
{
		FILE *f,*d;
	f=fopen("D:\\output.txt", "w");
	d=fopen("input.txt", "r");
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("D:\\output.txt");
	int n;
	char arr[4][4];
	bool O,X,_dot;
	O=X=_dot=false;
	in>>n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <4; j++)
			for (int k = 0; k < 4; k++)
			{
				in>>arr[j][k];
				if(arr[j][k]=='.')
					_dot=true;
			}
			int j=0;
			for (; j < 4; j++)
			{
				if((arr[j][0]=='X'||arr[j][0]=='T')&&(arr[j][1]=='X'||arr[j][1]=='T')&&(arr[j][2]=='X'||arr[j][2]=='T')&&(arr[j][3]=='X'||arr[j][3]=='T'))
				{X=true;goto hell;}
				if((arr[j][0]=='O'||arr[j][0]=='T')&&(arr[j][1]=='O'||arr[j][1]=='T')&&(arr[j][2]=='O'||arr[j][2]=='T')&&(arr[j][3]=='O'||arr[j][3]=='T'))
				{O=true;goto hell;}
				if((arr[0][j]=='X'||arr[0][j]=='T')&&(arr[1][j]=='X'||arr[1][j]=='T')&&(arr[2][j]=='X'||arr[2][j]=='T')&&(arr[3][j]=='X'||arr[3][j]=='T'))
				{X=true;goto hell;}
				if((arr[0][j]=='O'||arr[0][j]=='T')&&(arr[1][j]=='O'||arr[1][j]=='T')&&(arr[2][j]=='O'||arr[2][j]=='T')&&(arr[3][j]=='O'||arr[3][j]=='T'))
				{O=true;goto hell;}
			}
			if((arr[0][0]=='X'||arr[0][0]=='T')&&(arr[1][1]=='X'||arr[1][1]=='T')&&(arr[2][2]=='X'||arr[2][2]=='T')&&(arr[3][3]=='X'||arr[3][3]=='T'))
			{X=true;goto hell;}
			if((arr[0][3]=='X'||arr[0][3]=='T')&&(arr[1][2]=='X'||arr[1][2]=='T')&&(arr[2][1]=='X'||arr[2][1]=='T')&&(arr[3][0]=='X'||arr[3][0]=='T'))
			{X=true;goto hell;}
			if((arr[0][0]=='O'||arr[0][0]=='T')&&(arr[1][1]=='O'||arr[1][1]=='T')&&(arr[2][2]=='O'||arr[2][2]=='T')&&(arr[3][3]=='O'||arr[3][3]=='T'))
			{O=true;goto hell;}
			if((arr[0][3]=='O'||arr[0][3]=='T')&&(arr[1][2]=='O'||arr[1][2]=='T')&&(arr[2][1]=='O'||arr[2][1]=='T')&&(arr[3][0]=='O'||arr[3][0]=='T'))
			{O=true;goto hell;}


hell:	
	if(X)
		out<<"Case #"<<i+1<<": X won\n";
	else
	 {
		if(O)
			out<<"Case #"<<i+1<<": O won\n";
		else
		{
			if(_dot)
				out<<"Case #"<<i+1<<": Game has not completed\n";
			else
			{
				out<<"Case #"<<i+1<<": Draw\n";
			}
		}
	 } 
		O=X=_dot=false;
	}
	fclose(d);
	fclose(f);
	return 0;
}