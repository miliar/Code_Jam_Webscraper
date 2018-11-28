//begin

//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int greedrow = 0;
int greedcol=0;


int row=0;
int col = 0;

int set[105][105];

int start[105][105];
bool rowcol(int c, int d)
{
	int test = 0;
	bool pass = true;
	//from left to right
	for(int z = 0;z <col;z++)
	{
		if(start[c][d]<start[c][z])
		{
			pass= false;
			break;
		}
	}
	if(pass)
	{
			for(int z = 0;z <col;z++)
			{
				set[c][z] = start[c][d];
			}
			test =1;
	}

	pass =true;
	for(int z = 0;z <row;z++)
	{
		if(start[c][d]<start[z][d])
		{
			pass= false;
			break;
		}
	}
	//up down

	if(pass)
	{
		for(int z = 0;z <row;z++)
		{
			set[z][d] = start[c][d];
		}
		test = 1;
	}
	if (test == 1)
		return true;
	return false;
}
int greedy()
{
	int max = -1;
	greedrow = 0;
	greedcol = 0;
	for(int a=0;a<row;a++)
	{
		for(int b=0;b<col;b++)
		{
			if(start[a][b]>max && set[a][b] != start[a][b])
			{
				max = start[a][b];
				greedrow = a;
				greedcol = b;
			}
		}
	}
	return max;

}
int main()
{
	ofstream fout("problem.out");
	ifstream fin("problem.in");
	int cases=0;
	fin >> cases;
	row=0;col=0;greedrow=0;greedcol=0;
	for(int u=1;u<=cases;u++)
	{
		for(int qwe=0;qwe<100;qwe++)
		{
			for(int jj=0;jj<100;jj++)
			{
				start[qwe][jj] = 100;
			}

		}
		fin >> row >> col;

		for(int a=0;a<row;a++)
		{
			for(int b=0;b<col;b++)
			{
				fin >> start[a][b];
			}
		}
		int temp = greedy();
		for(int a=0;a<row;a++)
		{
			for(int b=0;b<col;b++)
			{
				set[a][b] = temp;
			}
		}
		bool hi = true;
		while(temp != -1)
		{
			temp = greedy();
			if(temp != -1)
			{
			if(!rowcol(greedrow,greedcol))
			{
				hi = false;
				break;
			}
			}
		}
		if(hi)
		{
			fout << "Case #" << u << ": YES\n";
		}
		else
		{
			fout << "Case #" << u << ": NO\n";
		}

		//end of big loop
	}
}