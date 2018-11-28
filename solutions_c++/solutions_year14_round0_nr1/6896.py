/*
 *  A.cpp
 *  
 *
 *  Created by Sushruth Muralidharan on 12/04/14.
 *  All rights reserved.
 *
 */
#include<iostream>
#include<fstream>
using namespace std;

int isunique(int A[4],int B[4])
{ int f=0,k=-1;
	for(int i=0;i<4;i++)
		for (int j=0; j<4; j++) {
			
			if(A[i]==B[j])
			{if(f==0)f=A[i]; else return -1;}
		}
	return f;	
	
}
int main()
{    
	int k,t,C1[4][4],C2[4][4],a1,a2,*A,*B;
	fstream fin,fout;
	fin.open("./A-small-attempt0.in",ios::in);
	fout.open("./Ao.txt",ios::out);
	fin>>t;
	for(k=0;k<t;k++)
	{ 
		fin>>a1;
		for(int i=0;i<4;i++)
			for (int j=0; j<4; j++) 
			{fin>>C1[i][j];
		
			}
		A = C1[a1-1];
		
		fin>>a2;
		for(int i=0;i<4;i++)
			for (int j=0; j<4; j++) 
			{fin>>C2[i][j];
				
			}
		B=C2[a2-1];
	
		fout<<"Case #"<<k+1<<": ";
		if(isunique(A,B)==-1) fout<<"Bad magician!";
		else if(isunique(A,B)==0) fout<<"Volunteer Cheated!";
		else fout<<isunique(A,B);
		fout<<endl;
	}
	
}


