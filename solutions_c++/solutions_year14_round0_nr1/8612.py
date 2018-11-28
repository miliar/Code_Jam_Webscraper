// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include<iostream>
#include<fstream>
#include<string>
using namespace std;
ifstream inFile;
ofstream outputFile;
void main()
{
	char s[1000],ch;
	int i=1,r1,r2,a[10],b[10],temp=0,count=0;

	streamsize n=1000;
	inFile.open("input.in", ios::in);
	outputFile.open("output.txt",ios::out|ios::trunc);
    inFile>>temp;
	while(inFile>>r1)
	{
		count =0 ;
		temp=r1;
		while((temp--))
			inFile>>a[0]>>a[1]>>a[2]>>a[3];
		temp=4-r1;
		while((temp--))
			inFile>>a[5]>>b[6]>>b[7]>>b[8];
		
		inFile>>r2;
		temp=r2;
		while((temp--))
			inFile>>b[0]>>b[1]>>b[2]>>b[3];
		temp=4-r2;
		while((temp--))
			inFile>>a[5]>>b[6]>>b[7]>>b[8];
		
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(a[j]==b[k])
				{
					count++;
					temp=a[j];
				}
		if(count==0)
			outputFile<<"Case #"<<i++<<": Volunteer cheated!";
		else if(count >1)
			outputFile<<"Case #"<<i++<<": Bad magician!";
		else
			outputFile<<"Case #"<<i++<<": "<<temp;
		outputFile<<"\n";
	}
}
