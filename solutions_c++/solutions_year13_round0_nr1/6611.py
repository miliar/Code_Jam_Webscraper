#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

int t, i, j, aux_t = 1, rez; 
char c[10][10], aux_char;

void compute()
{
	int contorX = 0, contorO = 0;
	bool incomplete = false;
	
	//Rows
	for(i=1; i<=4; i++)
	{
		contorO = contorX = 0;
		for(j=1; j<=4; j++)
			{
				if(c[i][j] == 'X')
					contorX++;
				else if(c[i][j] == 'O')
					contorO++;
				if(c[i][j] == 'T')
				{
					contorX++;
					contorO++;
				}
				if(c[i][j] == '.')
					incomplete = true;
			}	
		if(contorX == 4)
		{
			rez = 1;
			return;
		}
		if(contorO == 4)
		{
			rez = 2;
			return;
		}	
	}
	
	//Columns
	for(j=1; j<=4; j++)
	{
		contorO = contorX = 0;
		for(i=1; i<=4; i++)
			{
				if(c[i][j] == 'X')
					contorX++;
				else if(c[i][j] == 'O')
					contorO++;
				if(c[i][j] == 'T')
				{
					contorX++;
					contorO++;
				}
			}	
		if(contorX == 4)
		{
			rez = 1;
			return;
		}
		if(contorO == 4)
		{
			rez = 2;
			return;
		}
	}
	
	//Main diagonal
	contorX = 0, contorO = 0;
	for(i=1; i<=4; i++)
	{
		j = i;
		if(c[i][j] == 'X')
			contorX++;
		else if(c[i][j] == 'O')
			contorO++;
		if(c[i][j] == 'T')
		{
			contorX++;
			contorO++;
		}
	}
	if(contorX == 4)
	{
		rez = 1;
		return;
	}
	if(contorO == 4)
	{
		rez = 2;
		return;
	}
	
	//Second diagonal
	contorX = 0, contorO = 0;
	for(i=1; i<=4; i++)
	{
		j = 4-i+1;
		if(c[i][j] == 'X')
			contorX++;
		else if(c[i][j] == 'O')
			contorO++;
		if(c[i][j] == 'T')
		{
			contorX++;
			contorO++;
		}
	}
	if(contorX == 4)
	{
		rez = 1;
		return;
	}
	if(contorO == 4)
	{
		rez = 2;
		return;
	}	
		
	if(!incomplete)
		rez = 3;
	else
		rez = 0;
}

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	
	//Read
	fin>>t;
	
	
	//Compute
	while(aux_t <= t)
	{
		for(i=1; i<=4; i++)
			for(j=1; j<=4; j++)
				fin>>c[i][j];
			
		compute();
		switch(rez)
		{
			case 0: fout<<"Case #"<<aux_t<<": "<<"Game has not completed\n"; break;
			case 1: fout<<"Case #"<<aux_t<<": "<<"X won\n"; break;
			case 2: fout<<"Case #"<<aux_t<<": "<<"O won\n"; break;
			case 3: fout<<"Case #"<<aux_t<<": "<<"Draw\n"; break;
		}	
		aux_t++;
	}
}