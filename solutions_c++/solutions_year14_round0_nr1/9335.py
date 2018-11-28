/*
 * magic.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: lav
 */



#include<stdio.h>
#include<iostream>
#include<fstream>


using namespace std;
		int main(){

			ifstream infile;
			ofstream outfile;
			outfile.open("a.out");
	infile.open("a.in");
	int t;
	int first[4][4],second[4][4];
	int f,s;
	infile>>t;

	for(int tt=0;tt<t;tt++){
		infile>>f;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			infile>>first[i][j];
	infile>>s;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			infile>>second[i][j];

	int match=0,no=-1;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
			{

			if(first[f-1][i]==second[s-1][j])
			{
				//if(tt==0)cout<<first[f-1][i]<<"\t"<<second[s-1][j]<<"\n";
				match++; no=first[f-1][i];
			}
			}

	}


	if(match==1)
		outfile<<"Case #"<<tt+1<<": "<<no<<"\n";
	if(match>1)
		outfile<<"Case #"<<tt+1<<": "<<"Bad magician!"<<"\n";
	if(match<=0)
		outfile<<"Case #"<<tt+1<<": "<<"Volunteer cheated!"<<"\n";

	}
outfile.close();

		}
