// lawnmower.cpp : main project file.

// lawnmower.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

int smallCheck(int l,int b,int **lawn)
{
	int smallest = 101;
	int smallL;
	int smallB;
	for(int i=0; i<l;++i){
		for(int j=0; j<b;++j){
			if (smallest>lawn[i][j]){
				smallest=lawn[i][j];
				smallL = i;
				smallB = j;
			}
		}
	}
	if (smallest==101)
		return 2;
	for(int i=0;i<l;++i){

		if(lawn[i][smallB]!=101 && lawn[i][smallB]!=smallest)
		{
			
			for(int j=0;j<b;++j){
				if(lawn[smallL][j]!=101 && lawn[smallL][j]!=smallest){
					return 0;
				}
				if(j==b-1)
				{
					for(int jj=0;jj<b;++jj){
						lawn[smallL][jj]=101;
					}
						return 1;
					
				}
			}
		}
		if(i==l-1){
			for(int ii=0;ii<l;++ii){
						lawn[ii][smallB]=101;
			}
						return 1;
			
		}
	}
	

	return 2;
}



bool check(int l,int b, int **lawn){
	while(1){
		int check=smallCheck(l,b,lawn);
		if (check==0)
			return 0;
		if( check ==2)
			return 1;
	}
}





				




int main()
{
	int t;
	int l;
	int b;
	int **lawn;
	

	
	ifstream fp;
	ofstream fout;
	fp.open("input.txt",ios::beg);
	fout.open("output.txt",ios::beg);
	fp >> t;
	
	
	

	for(int i=0;i<t;++i){
		
		fp>>l;
		fp>>b;
		
		lawn = new int*[l];
		for(int len = 0; len < l; ++len)
			lawn[len] = new int[b];

		

		for(int j=0;j<l;++j){
			for(int k=0;k<b;++k){
				fp>>lawn[j][k];
			}
		}
		
		bool chack= check(l,b,lawn);
		if (chack==1)
			fout<<"Case #"<<i+1<<": YES"<<endl;
		else
			fout<<"Case #"<<i+1<<": NO"<<endl;
		delete lawn;
		
	}
	fp.close();
	fout.close();
	

	
}








	


