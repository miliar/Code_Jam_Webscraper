#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;

int optim_audience(int length, int audiences[])
{
	int result=0;
	int total_stands = 0;
	for(int i=0; i<length; i++)
	{
		if(total_stands<i)
		{
			int needed = i-total_stands;
			result+=needed;
			total_stands+=needed;
		}
		total_stands+=audiences[i];
	}
	return result;
}

int main()
{
	fstream fin("a.in",ios::in);
	fstream fout("a.out",ios::out);
	int max_tc;
	fin>>max_tc;
	int tc = 1;
	while(tc<=max_tc)
	{
		int result = 0;
		int length = 0;
		string audience="";
		fin>>length>>audience;
		length++;
		//string to int
		int audiences[1002]={0};
		for(int i = 0; i<length; i++)
		{
			audiences[i]=audience.at(i)-'0';
		}
		result= optim_audience(length,audiences);
		fout<<"Case #"<<tc<<": "<<result<<endl;
		tc++;
	}
	return 0;
}