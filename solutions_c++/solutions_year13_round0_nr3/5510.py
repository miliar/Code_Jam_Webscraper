// googlecj2013c.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int palinTest(unsigned long long n)	
{
	string s = std::to_string(n);
	string::iterator start=s.begin();
	string::iterator end=s.end()-1;
	bool b=(*start==*end);
	return b;
}

int squareTest(unsigned long long n)
{
	unsigned long long i=0;
	unsigned long long m=0;
	while(m<=n)
	{
		if(m==n)
		{
			if(palinTest(i))//平方根也要是迴文
				return 1;
		}
		++i;
		m=i*i;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	
	ifstream fin( "c:\\tinput.txt" );
	ofstream fout( "c:\\output.txt" , ios_base::in || ios_base::trunc);
	string temp1, temp2;
	istringstream stream1;
	string temp;
	fin>>temp;
	int times=0;
	unsigned long long numberBegin=0, numberEnd=0;
	stream1.str(temp);
	stream1>>times;
	string stc;
	getline(fin, stc);
	stream1.clear();
	for(int n=0; n<times; ++n)
	{	
		getline(fin, stc);
		//cout<<stc<<endl;
		stream1.str(stc);
		stream1>>numberBegin>>numberEnd;		
		stream1.clear();
		int count=0;
		for(unsigned long long k=numberBegin; k<=numberEnd; ++k)
		{
			if(palinTest(k))
				if(squareTest(k))
					++count;
		}
		fout<<"Case #"<<n+1<<": "<<count<<endl;
	}
	system("pause");
	return 0;
}

