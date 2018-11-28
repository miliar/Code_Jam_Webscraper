// codejam_2012_practice.cpp : Defines the entrO point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include<iostream>
#include "fstream"
using namespace std;
	  
int _tmain(int argc, _TCHAR* argv[])
{
	fstream f("problem_a.in",ios::in);	
	fstream g("problem_a.out",ios::out);
	int T;
	f>>T;
	int i,j;
	char test[4][4];
	int Xwl,Owl,Gw,Xw,Ow,Xwc,Owc;
	Xw=Ow=0;
	for(int t=1;t<=T;t++)
	{
	Xw=1;
	Owl=1;
	Xw=0;
	Ow=0;
	Gw=0;

	
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				{
					f>>test[i][j];
					if(test[i][j]=='.')Gw=1;
				}
		}

	

		if(
			((test[0][0]=='X')||(test[0][0]=='T'))&&
			((test[1][1]=='X')||(test[1][1]=='T'))&&
			((test[2][2]=='X')||(test[2][2]=='T'))&&
			((test[3][3]=='X')||(test[3][3]=='T'))	)
			Xw=1;
		else
		{
			if
				(((test[0][0]=='O')||(test[0][0]=='T'))&&
				((test[1][1]=='O')||(test[1][1]=='T'))&&
				((test[2][2]=='O')||(test[2][2]=='T'))&&
				((test[3][3]=='O')||(test[3][3]=='T'))	)
				Ow=1;

		}

		
		if(
			((test[0][3]=='X')||(test[0][3]=='T'))&&
			((test[1][2]=='X')||(test[1][2]=='T'))&&
			((test[2][1]=='X')||(test[2][1]=='T'))&&
			((test[3][0]=='X')||(test[3][0]=='T'))	)
			Xw=1;
		else
		{
			if
				(((test[0][3]=='O')||(test[0][3]=='T'))&&
				((test[1][2]=='O')||(test[1][2]=='T'))&&
				((test[2][1]=='O')||(test[2][1]=='T'))&&
				((test[3][0]=='O')||(test[3][0]=='T'))	)
				Ow=1;

		}

		
		if((Xw==0)&&(Ow==0))
		{ 
		for(i=0;i<4;i++)
		{  Xwc=Owc=Xwl=Owl=1;
			for(j=0;j<4;j++)
			{  
				if((test[j][i]=='O')||(test[j][i]=='T'));
				else Owc=0;

				if((test[j][i]=='X')||(test[j][i]=='T'));
				else Xwc=0;
				
					if((test[i][j]=='O')||(test[i][j]=='T'));
				else Owl=0;

				if((test[i][j]=='X')||(test[i][j]=='T'));
				else Xwl=0;
				
				
					
			}
			
			if(Xwc==1)Xw=1;
			if(Owc==1)Ow=1;
			if(Xwl==1)Xw=1;
			if(Owl==1)Ow=1;

		}
		
		
		}

		

		g<<"Case #"<<t<<": ";
		if(Xw==1)g<<"X won"<<endl;
		else
		if(Ow==1)g<<"O won"<<endl;
		if((Xw==0)&&(Ow==0)&&(Gw==1))g<<"Game has not completed"<<endl;
	if((Xw==0)&&(Ow==0)&&(Gw==0))
		g<<"Draw"<<endl;


			
	}
		return 0;
}

