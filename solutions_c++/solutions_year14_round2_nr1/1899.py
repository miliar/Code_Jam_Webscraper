#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
using namespace std;

#define STEP2

#ifdef STEP0
istream& fin = cin;
ostream& fout = cout;
#endif

#ifdef STEP1
ifstream fin ("A-sample.txt");
ostream& fout = cout;
#endif

#ifdef STEP2
ifstream fin ("A-small-attempt0.in");
ofstream fout ("A-small-attempt0.out");
#endif

#ifdef STEP3
ifstream fin ("A-large.in");
ofstream fout ("A-large.out");
#endif

bool isPossible(const vector<string>& str)
{
	for(int i=1; i<str.size(); i++)
	{
		if(str[i] != str[0])
			return false;
	}
	return true;
}

int calc(const vector<vector<int>>& data, int i)
{
	int rs = 1000;
	int N = data.size();
	
	int max = 1;
	for(int n=0; n<N; n++)
	{
		if(data[n][i] > max)
			max = data[n][i];
	}	
	
	for(int tar=1; tar<=max; tar++)
	{		
		int c = 0;
		for(int n=0; n<N; n++)
		{
			c += abs(data[n][i] - tar);
		}
		
		if(c < rs)
		{
			rs = c;
		}
	}
	
	return rs;
}

int main()
{
	int T;
	
	fin >> T;
	for(int t=1; t<=T; t++)
	{
		int N;		
		fin >> N;
		vector<string> strs(N);
		vector<string> uStrs(N);
		vector<vector<int>> data(N);
		vector<int> sum;
		
		for(int n=0; n<N; n++)
		{
			fin >> strs[n];
			
			int repeat = 1;
			char c = strs[n][0];
			for(int i=1; i<strs[n].size(); i++)
			{
				if(strs[n][i] != c)
				{
					data[n].push_back(repeat);
					uStrs[n] += c;
					repeat = 1;
					c = strs[n][i];
				}
				else
				{
					repeat++;
				}				
			}
			data[n].push_back(repeat);
			uStrs[n] += c;
		}
		
		fout << "Case #" << t << ": ";
		
		if(isPossible(uStrs))
		{
			int len = data[0].size();
			
			// sum
			/*
			for(int i=0; i<len; i++)
			{
				int s = 0;
				for(int n=0; n<N; n++)
				{
					s += data[n][i];
				}
				sum.push_back(s);
			}
			*/
			
			int rs = 0;
			for(int i=0; i<len; i++)
			{
				rs += calc(data, i);				
			}
			fout << rs;
		}
		else
		{
			fout << "Fegla Won";
		}
		
		fout << endl;
	}
	
	return 0;
}
