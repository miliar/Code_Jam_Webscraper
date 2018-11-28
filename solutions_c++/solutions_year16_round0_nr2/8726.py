/*
 * Revenge_of_Pancakes.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: neeraj
 */

#include<iostream>
#include <fstream>
using namespace std;

void ReverseAndFlip(string &str, int i)
{
	for (int k=0, j=i;k<=j;k++,j--)
	{
		char b;
		b= str[k]=='+'?'-':'+';
		str[k]= str[j]=='+'?'-':'+';
		str[j]=b;
	}
}


int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/B-large.in", ios::in);
	fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/B-large.out",ios::trunc);
	int t,c=0;
	fin>>t;

	while(t--)
	{
		c++;
		string str;
		fin>>str;
		int len = str.length();

		int res=0;
		char prevChar;
		while(1)
		{
			int j=1;
			prevChar = str[0];
			while(j<len && str[j]==prevChar)
			{
				j++;
			}
			if(prevChar=='+' && j==len)
				break;
			ReverseAndFlip(str,j-1);
			res++;
		}
		fout<<"Case #"<<c<<":"<<" "<<res<<endl;
	}
	return 0;
}
