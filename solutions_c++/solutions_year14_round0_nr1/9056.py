// googlecj2014a.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin( "c:\\A-small-attempt0.in" );
	ofstream fout( "c:\\output.txt" , ios_base::in || ios_base::trunc);
	string temp1, temp2;
	istringstream stream1;
	string temp;
	fin>>temp;
	stream1.str(temp);
	int times;
	stream1>>times;
	string stc;
	getline(fin, stc);
	stream1.clear();
	for(int i=0; i<times; ++i)
	{
		getline(fin, stc);
		stream1.clear();
		stream1.str(stc);
		int selected1=1;
		stream1>>selected1;
		//cout<<"selected1 "<<selected1<<"\n";
		vector<int> grid;
		vector<int> grid2;
		grid.resize(16);
		grid2.resize(16);
		for(int j=0; j<4; ++j)
		{
			getline(fin, stc);
			stream1.clear();
			stream1.str(stc);
			stream1>>grid[j*4+0]>>grid[j*4+1]>>grid[j*4+2]>>grid[j*4+3];
			//cout<<grid[j*4+0]<<" "<<grid[j*4+1]<<" "<<grid[j*4+2]<<" "<<grid[j*4+3]<<"\n";
		}
		getline(fin, stc);
		stream1.clear();
		stream1.str(stc);
		int selected2=1;
		stream1>>selected2;
		//cout<<"selected2 "<<selected2<<"\n";
		for(int j=0; j<4; ++j)
		{
			getline(fin, stc);
			stream1.clear();
			stream1.str(stc);
			stream1>>grid2[j*4+0]>>grid2[j*4+1]>>grid2[j*4+2]>>grid2[j*4+3];
			//cout<<grid[j*4+0]<<" "<<grid[j*4+1]<<" "<<grid[j*4+2]<<" "<<grid[j*4+3]<<"\n";
		}
		int sameTime=0;
		int theCard=0;
		for(int j=0; j<4; ++j)
		{
			for(int k=0; k<4; ++k)
			{
				if(grid[(selected1-1)*4+j]==grid2[(selected2-1)*4+k])
				{
					sameTime++;
					theCard=grid[(selected1-1)*4+j];
				}
			}
		}
		if(sameTime==1)
		{
			cout<<"Case #"<<i+1<<": "<<theCard<<"\n";
			fout<<"Case #"<<i+1<<": "<<theCard<<"\n";
		}
		else if(sameTime>1)
		{
			cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<"\n";
			fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<"\n";
		}
		else if(sameTime==0)
		{
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<"\n";
			fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<"\n";
		}
		//cout<<"same times "<<sameTime<<" the card "<<theCard<<"\n";
	}
	//system("pause");
	return 0;
}

