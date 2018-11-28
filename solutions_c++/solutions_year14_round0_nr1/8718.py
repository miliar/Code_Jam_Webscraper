//============================================================================
// Name        : magic.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

ofstream fout("out.txt"),fout2("output.txt");
ifstream fin("A-small-attempt0.in");
int main() {


	int matrix1[4][4],matrix2[4][4];
	int arr1[4],arr2[4];
	int i,y,x,test,r1,r2,flag=0,no=0,chaet=0;

	fin>>test;
	for(i=0;i<test;i++)
	{	flag=0;no=0;chaet=0;
		fin>>r1;
		r1--;
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				fin>>matrix1[x][y];
			}
		}
		fin>>r2;
		r2--;
			for(x=0;x<4;x++)
			{
				for(y=0;y<4;y++)
				{
					fin>>matrix2[x][y];
				}
			}
		for(x=0;x<4;x++)
		{
			arr1[x]=matrix1[r1][x];
			arr2[x]=matrix2[r2][x];
		}
fout<<"\ncase"<<i+1<<" r1"<<r1<<" r2"<<r2;
		for(x=0;x<4;x++)
				{
					fout<<"\n"<<arr1[x]<<" "<<arr2[x];
				}
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				if(arr1[x]==arr2[y])
				{

						flag++;
						no=arr1[x];


				}
			}
		}
		if(flag==0)
		{
			fout2<<"\nCase #"<<i+1<<": Volunteer cheated!";
		}
		else
		{
			if(flag==1)
				fout2<<"\nCase #"<<i+1<<": "<<no;
			else
				fout2<<"\nCase #"<<i+1<<": Bad magician!";
		}
	}

	return 0;
}
