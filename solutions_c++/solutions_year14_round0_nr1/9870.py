// contest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
void compare(int array1 [],int array2[],ofstream& out_file,int Case)
{

	int found=0;
	int count=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(array1[i]==array2[j])
			{
				found=array2[j];
				count++;
			}
		}
	}
	if(count>1)
	{
		out_file<<"Case #"<<Case<<": "<<"Bad magician!"<<endl;
	}
	else if(count==0)
	{
		out_file<<"Case #"<<Case<<": "<<"Volunteer Cheated!"<<endl;
	}
	else
	{
		out_file<<"Case #"<<Case<<": "<<found<<endl;
	}
}

void magic(ifstream& in_file,ofstream& out_file,int inputs)
{
	int first_selection=0;
	int second_selection=0;
	int first_row [4]={};
	int second_row [4]={};
	int arrangement1[4][4]={};
	int arrangement2[4][4]={};
	in_file>>first_selection;
	first_selection--;
	for(int x=0;x<4;x++)
	{
		for (int j = 0; j < 4; j++)
		{
			in_file>>arrangement1[x][j];
		}
		
	}
	in_file>>second_selection;
	second_selection--;
	for(int x=0;x<4;x++)
	{
		for (int j = 0; j < 4; j++)
		{
			in_file>>arrangement2[x][j];
		}
		
	}
	for(int i=0;i<4;i++)
	{
		first_row[i]=arrangement1[first_selection][i];
		second_row[i]=arrangement2[second_selection][i];
	}
	compare(first_row,second_row,out_file,inputs);
}

int main()
{
	int total_inputs=0;
	int arrangement1[4][4]={};
	int arrangement2[4][4]={};
	ofstream out_file;
	out_file.open("C:\\Users\\malik\\Downloads\\Output.txt");
	ifstream in_file;
	in_file.open("C:\\Users\\malik\\Downloads\\A-small-attempt3.in");
	in_file>>total_inputs;
	int first_selection=0;
	int second_selection=0;
	for(int i=1;i<total_inputs+1;i++)
	{
		magic(in_file,out_file,i);	
	}
	return 0;
}

