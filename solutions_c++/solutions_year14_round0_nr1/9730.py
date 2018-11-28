// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include<conio.h>
#include<iostream>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	fstream f("pba.txt",ios::in);
fstream g ("pbaout3",ios::out);
	int g1,g2,i,j,m,n,nr=0,mat[5][5],mat2[5][5], pos[5], card,nc,line;
	int numberoftestcases=0;
	line =1;
	f>>numberoftestcases;
	while(line<=numberoftestcases)
	{
		card = -1;
		nc=0;
		f>>g1;
	
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				f>>mat[i][j];
	
		j=1;
		for(i = g1;i<=4;i++) 
			pos[j++]=mat[i][j];

		f>>g2;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				f>>mat2[i][j];
	for( i =1 ; i<=4;i++)
	{
		for(j=1;j<=4;j++)
		{
			if( mat[g1][i]  == mat2[g2][j] )
				{card = mat[g1][i];
			 nc++;
			}}
	}

		g<<"Case #"<<line<<": ";
		
		if(( card != -1 ) &&( nc == 1 ) )
			g<<card<<endl;
		if((card!=-1)&&(nc>1))
			g<<"Bad magician!"<<endl;
		
			if((  card == -1)  && (nc == 0 ))
				g<<"Volunteer cheated!"<<endl;
		line++;
		card = -1;
		nc=0;

	}
	

	return 0;
}

