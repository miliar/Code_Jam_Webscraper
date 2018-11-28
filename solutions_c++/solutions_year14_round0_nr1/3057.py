// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int n,no1,no2,row1[4],row2[4],garbage,flag=0,ans;
	ifstream fin ("C:\\file\\A-small-attempt0.in");
	ofstream fout ("C:\\file\\A-small-attempt0.out");
	fin>>n;
	for(int i = 0 ; i<n;i++)
	{
		fin>>no1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(no1==(j+1))
				{
					fin>>row1[k];
				}
				else
					fin>>garbage;
			}
		}
		fin>>no2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(no2==(j+1))
				{
					fin>>row2[k];
				}
				else
					fin>>garbage;
			}
		}
		fout<<"Case #"<<(i+1)<<": ";
		for(int j=0; j<4;j++)
		{
			for(int k=0; k<4;k++)
			{
				if(row1[j]==row2[k])
				{
					flag++;
					ans=row1[j];
					break;
				}
			}
		}
		if(flag==0)
			fout<<"Volunteer cheated!";
		else if(flag==1)
			fout<<ans;
		else if(flag>1)
			fout<<"Bad magician!";
		if((i+1)!=n)
			fout<<endl;
		flag=0;
	}
	return 0;
}

