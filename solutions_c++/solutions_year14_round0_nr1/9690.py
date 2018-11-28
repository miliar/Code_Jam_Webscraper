// Google code jam - magic trick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

void processinput(char input[], int possiblenumbers[]);

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream output;
	ifstream input;

	int possiblenumbers[4];
	int chosennumbers[4],chosennumbers2[4];
	char cards[100];
	int cardnumber, matches;
	int i,j,k;

	int numberofcases, userrow;

	input.open("test.txt");
	output.open("output.txt");

	if(!input||!output)
	{
		cout<<"error, file not found";
		return 0;
	}
	input>>numberofcases;
	for(int counter=0;counter<numberofcases;counter++)
	{
		matches=0;
		cardnumber=0;
		input>>userrow;
		for(int counter2=0;counter2<4;counter2++)
		{
			input>>possiblenumbers[0]>>possiblenumbers[1]>>possiblenumbers[2]>>possiblenumbers[3];
			if(userrow==(counter2+1))
			{
				chosennumbers[0]=possiblenumbers[0];
				chosennumbers[1]=possiblenumbers[1];
				chosennumbers[2]=possiblenumbers[2];
				chosennumbers[3]=possiblenumbers[3];
			}
		}
		input>>userrow;
		for(int counter2=0;counter2<4;counter2++)
		{
			input>>possiblenumbers[0]>>possiblenumbers[1]>>possiblenumbers[2]>>possiblenumbers[3];
			if(userrow==(counter2+1))
			{
				chosennumbers2[0]=possiblenumbers[0];
				chosennumbers2[1]=possiblenumbers[1];
				chosennumbers2[2]=possiblenumbers[2];
				chosennumbers2[3]=possiblenumbers[3];
			}
		}

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(chosennumbers[i]==chosennumbers2[j])
				{
					cardnumber=chosennumbers[i];
					matches++;
				}
			}
		}
		output<<"Case #"<<counter+1<<": ";
		if(matches==0)
			output<<"Volunteer cheated!"<<endl;
		if(matches==1)
			output<<cardnumber<<endl;
		if(matches>1)
			output<<"Bad magician!"<<endl;

	}
	return 0;
}