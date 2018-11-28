// TicTacToe.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
enum
{
	WIN_X,
	WIN_O,
	WIN_DRAW,
	WIN_NOTEDED,

};

int size(4);

int CheckDiagonal(vector<string>& data, int& e)
{
	int cX(0),cO(0),cE1(0);
	for(int i=0;i<::size;i++)
	{
		if(data[i][i]=='X')
		{
			cX++;
		}
		if(data[i][i]=='O')
		{
			cO++;
		}
		if(data[i][i]=='.')
		{
			cE1++;
		}
	}
	if(cX==0 && cE1==0){ return WIN_O;}
	if(cO==0 && cE1==0){ return WIN_X;}
	
	cX = 0; cO = 0; int cE2(0);
	for(int i=0;i<::size;i++)
	{
		if(data[i][::size-i-1]=='X')
		{
			cX++;
		}
		if(data[i][::size-i-1]=='O')
		{
			cO++;
		}
		if(data[i][::size-i-1]=='.')
		{
			cE2++;
		}
	}
	if(cX==0 && cE2==0){ return WIN_O;}
	if(cO==0 && cE2==0){ return WIN_X;}

	e += cE1+cE2;

	return WIN_DRAW;
}

int CheckCol(vector<string>& data, int& e)
{
	int cX(0),cO(0),cE1(0);
	for(int i=0;i<::size;i++)
	{
		cX = 0;cO=0;cE1=0;
		for(int j=0;j<::size;j++)
		{
			if(data[j][i]=='X')
			{
				cX++;
			}
			if(data[j][i]=='O')
			{
				cO++;
			}
			if(data[j][i]=='.')
			{
				cE1++;
			}
		}
		e += cE1;
		if(cX==0 && cE1==0){ return WIN_O;}
		if(cO==0 && cE1==0){ return WIN_X;}
	}
	
	return WIN_DRAW;
}

int CheckRow(vector<string>& data, int& e)
{
	int cX(0),cO(0),cE1(0);
	for(int i=0;i<::size;i++)
	{
		cX = 0;cO=0;cE1=0;
		for(int j=0;j<::size;j++)
		{
			if(data[i][j]=='X')
			{
				cX++;
			}
			if(data[i][j]=='O')
			{
				cO++;
			}
			if(data[i][j]=='.')
			{
				cE1++;
			}
		}
		e += cE1;
		if(cX==0 && cE1==0){ return WIN_O;}
		if(cO==0 && cE1==0){ return WIN_X;}
	}

	return WIN_DRAW;
}

int _tmain(int argc, _TCHAR* argv[])
{	
	int qnt(0);
	//string qnt;
	ifstream myReadFile;
	myReadFile.open("D:/Downloads/A-large.in");
	ofstream fout;
	fout.open("D:/Sources/GoogleCodeJam/qualification/TicTacToe/output.txt");

	if (myReadFile.is_open()) {		
		myReadFile >> qnt;
		for(int i=0;i<qnt;i++)
		{				
			vector<string> data;
			for(int j=0;j<size;j++)
			{
				string line;
				myReadFile >> line;
				data.push_back(line);
				//fout << line<< endl;
			}
			{
				int e(0);
				int ret(WIN_DRAW);
				ret = CheckRow(data,e);
				if(ret==WIN_X){ fout << "Case #"<< i+1 <<": X won" << endl; continue;}
				if(ret==WIN_O){fout << "Case #"<< i+1 <<": O won" << endl;continue;}				
				ret = CheckCol(data,e);
				if(ret==WIN_X){ fout << "Case #"<< i+1 <<": X won" << endl; continue;}
				if(ret==WIN_O){fout << "Case #"<< i+1 <<": O won" << endl;continue;}				
				ret = CheckDiagonal(data,e);
				if(ret==WIN_X){ fout << "Case #"<< i+1 <<": X won" << endl; continue;}
				if(ret==WIN_O){fout << "Case #"<< i+1 <<": O won" << endl;continue;}
				if(ret==WIN_DRAW){
					if(e!=0){fout << "Case #"<< i+1 <<": Game has not completed" << endl; continue;}
					else{ fout << "Case #"<< i+1 <<": Draw" << endl; continue;}
				}
			}
			
			
			string emp;
			myReadFile >> emp;
		}
		
	}
		
	return 0;
}

