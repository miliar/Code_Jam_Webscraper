// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <numeric>

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include<algorithm>
#include<iomanip> 


using namespace std;
#define FOR(i, a, b) for(i = (a); i < (b); ++i)

const double pi = 3.1415926535897;

vector<int> data;
FILE* fin;
FILE* fout;

#include<fstream> 
#include<iostream> 
#include<string> 
using namespace std; 

vector<int> alldata;
vector<string> vs;

char* file_input="A-small-attempt0.in";
char* file_output="out.in";


void main() 
{ 
	ofstream outFile; 
	outFile.open(file_output); 

	ifstream inFile; 
	inFile.open(file_input); 

	string str; 
	int cnt=0;
	int T=0; //test Case number

	if (! inFile.is_open())  
	{ 
		cout << "Error opening file"; 
		exit (1);
	} 

	string line;
	int first;
	int second;
	int data[4][4];
	int data1[4][4];
	while ( getline(inFile, line) ) 
	{
		if(cnt ==0 )
		{
			istringstream ss(line);
			ss>>T;
			cnt++;
			continue;			
		}
		else
		{
			istringstream ss(line);
			ss>>first;
			for (int i=0; i<4;i++)
			{
				getline(inFile, line);
				istringstream ss1(line);
				for (int j=0;j<4;j++)
				{
					ss1>> data[i][j];
				}				
			}
			getline(inFile, line);
			istringstream ss2(line);
			ss2>>second;
			for (int i=0; i<4;i++)
			{
				getline(inFile, line);
				istringstream ss1(line);
				for (int j=0;j<4;j++)
				{
					ss1>> data1[i][j];
				}				
			}
			cnt ++;
			// compute
			vector<vector<int>> rst;
			int id;
			int flag=0;
			for (int j= 0; j<4;j++)
			{
				int p = data[first-1][j];
				vector<int> tmp;
				//check
				for (int m=0; m <4; m++)
				{
					if (p==data1[second-1][m])
					{
						tmp.push_back(p);
					}
				}
				rst.push_back(tmp);
				if (tmp.size()==1)
				{
					id =p;
					flag++;
				}
			}

			if (flag==0)
			{
				outFile << "Case #" << cnt-1<<": "<<"Volunteer cheated!"<<endl;
			}
			else if (flag==1)
			{
				outFile << "Case #" << cnt-1<<": "<<id<<endl;
			}
			else
			{
				outFile << "Case #" << cnt-1<<": "<<"Bad magician!"<<endl;
			}

		}

	}

	inFile.close(); 
	outFile.close(); 
}


