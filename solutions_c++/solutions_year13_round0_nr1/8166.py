// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<stdio.h>
#include<fstream>
#include<iostream>
#include<fileapi.h>
int mark[10][4][4];//0=blank, 1=X, 2=O, 3=T
bool checkRows(int k,int x)
{
	for (int i = 0; i < 4; i++)
	{
		
			if(mark[k][i][0]==x&&mark[k][i][1]==x&&mark[k][i][2]==x&&mark[k][i][3]==x)
				return true;
		
	}
	return false;
}
bool checkCols(int k,int x)
{
	
	for (int i = 0; i < 4; i++)
	{
		
			if(mark[k][0][i]==x&&mark[k][1][i]==x&&mark[k][2][i]==x&&mark[k][3][i]==x)
				return true;
		
	}
	return false;
}
bool checkDiag(int k,int x)
{
	if(mark[k][0][0]==x&&mark[k][1][1]==x&&mark[k][2][2]==x&&mark[k][3][3]==x)
				return true;
	if(mark[k][0][3]==x&&mark[k][1][2]==x&&mark[k][2][1]==x&&mark[k][3][0]==x)
				return true;
	return false;
}
bool checkOwins(int k)
{
	
	if(checkRows(k,2)||checkCols(k,2)||checkDiag(k,2))
		return true;
	return false;
}

bool checkXwins(int k)
{
	if(checkRows(k,1)||checkCols(k,1)||checkDiag(k,1))
		return true;
	return false;
}

bool isGameNotOver(int k)
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if(mark[k][i][j]==0)
				return true;
		}
	}
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int ncases;
	int endcase; //0=null, 1=x wins, 2= O wins, 3= draw, 4= game not over.
	
	scanf_s("%d",&ncases);

	for(int k=0;k<ncases;k++)
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		scanf_s("%d",&mark[i][j]);

	for(int k=0;k<ncases;k++)
	{
		if(checkOwins(k))
			endcase=2;
		else if(checkXwins(k))
			endcase=1;
		else if (isGameNotOver(k))
			endcase=4;
		else
		{
			endcase=3;
		}
		printf("\nCase #%d",k+1);
		switch (endcase)
	{
	case 0: printf("error");
		break;
	case 1: printf("X Won");
		break;
	case 2: printf("O Won");
		break;
	case 3: printf("Draw");
		break;
	case 4: printf("Game has not completed");
		break;
	default:
		break;
	}

	}

	



}

