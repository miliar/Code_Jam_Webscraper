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

vector<double> d;
vector<string> vs;

char* file_input="D-large.in";
char* file_output="D-large.out";
//char* file_input="test.txt";
//char* file_output="out.txt";


bool complare(double a, double b)
{
	return a>b;
}

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
	double rst1 = 0;
	double rst2 = 0;
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
			vector<double> d1;
			vector<double> d2;
			double tmp;
			int N;
			istringstream ss(line);
			ss>>N;
			getline(inFile, line);
			istringstream ss1(line);
			for (int i=0; i<N;i++)
			{
				ss1>>tmp;
				d1.push_back(tmp);
			}
			getline(inFile, line);
			istringstream ss2(line);
			for (int i=0; i<N;i++)
			{
				ss2>>tmp;
				d2.push_back(tmp);
			}
			cnt ++;

			// compute
			sort(d1.begin(), d1.end(),complare); 
			sort(d2.begin(), d2.end(),complare); 
			vector<double> d2_tmp = d2;
			vector<double> d1_tmp = d1;
			int count = 0;

			int t=0;
			while (d1.size())
			{
				double p = d1[0];
				if (p>d2[0])
				{
					d1.erase(d1.begin());
					d2.erase(d2.begin());
					count++;
				}
				else
				{
					d1.erase(d1.begin()+d1.size()-1);
					d2.erase(d2.begin());
				}

			}

			rst1 = count;

			d1 = d1_tmp;
			d2 = d2_tmp;
			count = 0;
			sort(d2.begin(), d2.end()); 
			sort(d1.begin(), d1.end()); 
			for (int i=0;i<N;i++)
			{
				double p = d1[i];
				for (int j=0;j<d2.size();j++)
				{
					if (d2[j]>p)
					{
						d2.erase(d2.begin()+j);
						count++;
						break;						
					}
				}
			}
			rst2 = N - count;

			outFile << "Case #" << cnt-1<<": "<<rst1<<" "<<rst2<<endl;	
		}
	}

	inFile.close(); 
	outFile.close(); 
}


