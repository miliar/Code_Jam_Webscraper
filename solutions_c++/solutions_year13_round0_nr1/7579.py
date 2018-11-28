// te.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include <math.h>
using namespace std;

string CompareSting(char C[4][4])
{
	int X=0,O=0;
	int countH=0,countV=0,countHV=0,countVH=0;
	string res="";
	int mark=0;
	for (int i=0;i<4;i++)
	{
		countH=0;
		countV=0;
		for (int j=0;j<4;j++)
		{
			if (C[i][j]=='.')
			{
				mark=1;
			}
			if (C[i][j]=='X'||C[i][j]=='T')
			{
				countH++;
			}
			if (C[j][i]=='X'||C[j][i]=='T')
			{
				countV++;
			}
		}
		if (C[i][i]=='X'||C[i][i]=='T')
		{
			countHV++;
		}
		if (C[i][3-i]=='X'||C[i][3-i]=='T')
		{
			countVH++;
		}
		if (countH==4||countV==4||countHV==4||countVH==4)
		{
			res="X won";
			return res;
		}
	}

	countHV=0;
	countVH=0;
	for (int i=0;i<4;i++)
	{
		countH=0;
		countV=0;
		for (int j=0;j<4;j++)
		{
			if (C[i][j]=='O'||C[i][j]=='T')
			{
				countH++;
			}
			if (C[j][i]=='O'||C[j][i]=='T')
			{
				countV++;
			}
		}
		if (C[i][i]=='O'||C[i][i]=='T')
		{
			countHV++;
		}
		if (C[i][3-i]=='O'||C[i][3-i]=='T')
		{
			countVH++;
		}
		if (countH==4||countV==4||countHV==4||countVH==4)
		{
			res="O won";
			return res;
		}
	}

	if (mark)
	{
		res="Game has not completed";
		return res;
	}else
	{
		res="Draw";
		return res;
	}


}
int main()
{
	int T;
	char C[4][4];
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	cin>>T;
	for(int i=0;i<T;i++)
	{
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				cin>>C[i][j];
			}
		}

		cout<<"Case #"<<i+1<<": "<<CompareSting(C)<<endl;
	}

	return 0;

}