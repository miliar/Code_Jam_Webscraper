#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

string  arr[4];

int r=0,colum=0,d=0;

int i=0,j=0 ;
bool draw;

char row(int i)
{
	int r=0,col=0,d=0;
	bool c=false;
	for(j=0; j<4; j++)
	{
		switch(arr[i].at(j))
		{
		case 'X':
			r += 1;
			break;
		case 'O':
			r += 10;
			break;
		case 'T':
			c = true;
			break;
		case '.':
			draw = false;
		}
	}
	switch(r)
	{
	case 3:
		if(c)return 'X';
		break;
	case 4:
		return 'X';
		break;
	case 30:
		if(c)return 'O';
		break;
	case 40:
		return 'O';
		break;
	}
	return 'N';
}

char col(int i)
{
	int r=0,col=0,d=0;
	bool c=false;
	for(j=0; j<4; j++)
	{
		switch(arr[j].at(i))
		{
		case 'X':
			r += 1;
			break;
		case 'O':
			r += 10;
			break;
		case 'T':
			c = true;
			break;
		case '.':
			draw = false;

		}
	}
	switch(r)
	{
	case 3:
		if(c)return 'X';
		break;
	case 4:
		return 'X';
		break;
	case 30:
		if(c)return 'O';
		break;
	case 40:
		return 'O';
		break;
	}
	return 'N';
}

char dia_left()
{
	int r=0,col=0,d=0;
	bool c=false;
	for(i=0,j=0; j<4; i++,j++)
	{
		switch(arr[i].at(j))
		{
		case 'X':
			r += 1;
			break;
		case 'O':
			r += 10;
			break;
		case 'T':
			c = true;
			break;
		case '.':
			draw = false;
		}
	}
	switch(r)
	{
	case 3:
		if(c)return 'X';
		break;
	case 4:
		return 'X';
		break;
	case 30:
		if(c)return 'O';
		break;
	case 40:
		return 'O';
		break;
	}
	return 'N';
}

char dia_right()
{
	int r=0,col=0,d=0;
	bool c=false;
	for(i=0,j=3; i<4; i++,j--)
	{
		switch(arr[i].at(j))
		{
		case 'X':
			r += 1;
			break;
		case 'O':
			r += 10;
			break;
		case 'T':
			c = true;
			break;
		case '.':
			draw = false;
		}
	}
	switch(r)
	{
	case 3:
		if(c)return 'X';
		break;
	case 4:
		return 'X';
		break;
	case 30:
		if(c)return 'O';
		break;
	case 40:
		return 'O';
		break;
	}
	return 'N';
}
int main()
{
	ifstream fin ("in.txt");
	ofstream fcout("out.txt");
	int n,k=0;
	
	fin>>n;

	while(k<n)
	{
		draw = true;
		bool f=true;
		for(i=0; i<4; i++)
			fin>>arr[i];
		k++;
		for(i=0; i<4; i++)
		{
			if (row(i)=='X' || col(i)=='X')
			{fcout << "Case #" << k << ": X won\n" ;f=false;break;}
			else if(row(i)=='O' || col(i)=='O')
			{fcout << "Case #" << k << ": O won\n" ;f=false;break;}
		}

		if(f)
		{
			if (dia_left()=='X' || dia_right()=='X')
			{fcout << "Case #" << k << ": X won\n" ;f=false;}
			else if(dia_left()=='O' || dia_right()=='O')
			{fcout << "Case #" << k << ": O won\n" ;f=false;}
		}
		if(f)
		{
			if(draw)
				fcout << "Case #" << k <<": Draw\n";
			else 
				fcout << "Case #" << k <<": Game has not completed\n";
		}

	}
	return 0;
}