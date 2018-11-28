#include "stdafx.h"
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	const int n=4;
	int t,str_1,str_2,set_1[n][n],set_2[n][n];
	fin>>t;
	int m,card;
	for(int i=0;i<t;i++)
	{
		m=0;
		fin>>str_1;
		str_1--;
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
				fin>>set_1[j][k];
		fin>>str_2;
		str_2--;
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
				fin>>set_2[j][k];
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
				if(set_1[str_1][j]==set_2[str_2][k])
				{
					m++;
					card=set_1[str_1][j];
				}
		fout<<"Case#"<<i+1<<": ";
		switch(m)
		{
			case 0:fout<<"Volunteer cheated!";break;
			case 1:fout<<card;break;
			default:fout<<"Bad magician!";
		}
		fout<<endl;
	}
	return 0;
}