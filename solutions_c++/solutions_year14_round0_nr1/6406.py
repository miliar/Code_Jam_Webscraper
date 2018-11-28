// Magic_trick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-small-attempt0.in");
	ofstream out("otput.txt");
	int numTc;
	in>>numTc;
	for(int i=0;i<numTc;i++)
	{
		int ans1;
		in>>ans1;
		int first[4][4];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				in>>first[j][k];
			}
		}
		int ans2;
		in>>ans2;
		int second[4][4];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				in>>second[j][k];
			}
		}
		int numCards=0;
		int num=-1;
		for(int l=0;l<4;l++)
		{
			for(int m=0;m<4;m++)
			{
				if(first[ans1-1][l]==second[ans2-1][m])
				{
					numCards++;
					num = first[ans1-1][l];
				}

			}
		}
		if(numCards==0)
		{
			out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else if(numCards==1)
		{
			out<<"Case #"<<i+1<<": "<<num<<endl;
		}
		else
		{
			out<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
	}
	return 0;
}

