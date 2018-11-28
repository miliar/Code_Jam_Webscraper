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

char* file_input="B-large.in";
char* file_output="B-large.out";
//char* file_input="test.txt";
//char* file_output="out.txt";


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
	double d[3];
	double rst;
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
			for (int i=0; i<3;i++)
			{
				ss>>d[i];					
			}
			cnt ++;
			// compute
			if (d[2]<d[0])
			{
				rst =  d[2]/2;
			}
			else
			{
				rst = 0;
				int cout=0;
				double s = 2 + cout*d[1];
				double t0 = d[2]/s;
				double t1 = d[0]/2 + d[2]/(2 + (cout+1)*d[1]);

				if (t0==t1 || t0<t1)
				{
					rst = t0;
					outFile << "Case #" << cnt-1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<rst<<endl;
					continue;
				}
				while(t0 > t1)
				{
					cout ++;
					t0 = d[2]/s;					
					t1 = d[0]/s + d[2]/(2 + cout*d[1]);
					s = 2 + cout*d[1];					
				}
				cout--;
				for (int i =0 ;i< cout;i++)
				{
					rst+= d[0]/(2 + i*d[1]);
				}
				rst+= d[2]/(2 + cout*d[1]);
				
			}

			outFile << "Case #" << cnt-1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<rst<<endl;			

		}

	}

	inFile.close(); 
	outFile.close(); 
}


