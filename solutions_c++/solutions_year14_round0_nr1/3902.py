#include <cstdlib>
#include <iostream>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <fstream>
using namespace std;

ofstream myAns;
ifstream Qfile;


int MAP[4][4]={0};

void ReadMap(int choiseRow,int *RowNums)
{
	int c,r;
	for(r=0;r<4;r++)
	{
		for(c=0;c<4;c++)
		{
			Qfile>>MAP[r][c];
			if(r+1==choiseRow)
			{
				RowNums[c]=MAP[r][c];
			}
		}	
	}
}

void Solve(int CaseNum)
{
	int WhitchRowFirst,WhitchRowSecond;
	int FirstRowNums[4]={0};
	int SecondRowNums[4]={0};
	int c1=0,c2=0;
	int TheAnsNumber=0;
	int HowManySame=0;

	Qfile>>WhitchRowFirst;
	ReadMap(WhitchRowFirst,FirstRowNums);

	Qfile>>WhitchRowSecond;
	ReadMap(WhitchRowSecond,SecondRowNums);

	for(c1=0;c1<4;c1++)
	{
		for(c2=0;c2<4;c2++)
		{
			if(FirstRowNums[c1]==SecondRowNums[c2])
			{
				TheAnsNumber=FirstRowNums[c1];
				HowManySame++;
			}
		}	
	}


	myAns<<"Case #"<<CaseNum<<": ";
	if(HowManySame==0)
	{
		myAns<<"Volunteer cheated!";
	}
	else if(HowManySame>=2)
	{
		myAns<<"Bad magician!";
	}
	else if(HowManySame==1)
	{
		myAns<<TheAnsNumber;
	}
	myAns<<endl;
}

int main(int argc, char *argv[])
{
	int T=0;
	int i=0;

	Qfile.open("A-small-attempt0.in");
	myAns.open ("MyAnser.txt");
		
	Qfile>>T;
	
	
	for(i=0; i<T; i++)	
	{						
		Solve(i+1);
	}
	myAns.close();
	Qfile.close();
    
	system("PAUSE");
    return EXIT_SUCCESS;
}
