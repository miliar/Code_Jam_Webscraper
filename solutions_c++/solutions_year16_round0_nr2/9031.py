#include <stdafx.h>
#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
using namespace std;
void flip(string &str,int start,int end)
{
	for(int i = start; i<=end;i++)
	{
		if(str.at(i)=='+')
		{
			str.at(i)='-';
		}
		else
		{
			str.at(i)='+';
		}
	}
}
int main() {
	int testcases=0;
	string str("");

	unsigned long N=0;


	ofstream f;
	f.open("D:\\algo\\google code jam\\Revenge of the Pancakes upload\\pancake.txt",ios::app);

	cin>>testcases;

	for(int t=1;t<=testcases;t++)
	{
		cin>>str;	
		str.erase(remove(str.begin(),str.end(),' '),str.end());
		int ncount=0,start=0;
		int length = str.length();
		bool bsign = false;
		char c;

		if(length>0)
		{
			if(str[0]=='-')
			{
				bsign = false;
				c='-';
			}
			else
			{
				bsign = true;
				c='+';
			}
		}
		for(int i=1;i<length;i++)
		{
			if(str[i] != c)
			{
				ncount++;
				//flip(str,start,i-1);
				c= str[i];
			}
			else
			{
				if(c=='+')
				str[i] = '-';
				else
					str[i] = '+';
			}
		}
		if(c=='-')
		{
			ncount++;
		}
		f<<"Case #"<<t<<": "<<ncount<<endl;
	}
	f.close();

	return 0;
}