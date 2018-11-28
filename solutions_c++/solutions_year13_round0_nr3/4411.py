#include<algorithm>
#include<iostream>
#include<vector>
#include<cmath>
#include<stdio.h>
#include<fstream>
using namespace std;
vector<int> paldome;
bool ispal()
{
	int r=paldome.size();
	for(int i=0;i<=(r-1)/2;i++)
	{
		if(paldome.at(i)==paldome.at(r-i-1))
		{
		}
		else
		{
			return false;
		}
	}
	return true;
}
int main()
{
	fstream fin("mow.txt");
	fstream fout("out.txt", ios::out);
	int T;
	fin>>T;
	for(int round=1;round<=T;round++)
	{
		long long A,B;
		fin>>A>>B;
		long long sqA=(long long)(sqrt(A));
		long long sqB=(long long)(sqrt(B));
		long long count=0;
	//	fout<<sqA<<endl<<sqB<<endl;
		for(long long i=sqA;i<=sqB;i++)
		{
			paldome.clear();
		    long long number=i;
		    while(number>0)
		    {
		    	paldome.push_back(number%10);
		    	number=number/10;
		    }
		    if(ispal())
		    {
		    	paldome.clear();
		    	number=i*i;
		    	long long temp=number;
		    	while(number>0)
		    	{
		    	paldome.push_back(number%10);
		    	number=number/10;
		    	}
		    	if(ispal()&&temp>=A&&temp<=B)
		    	{
		    		count++;
		    	}
		    }
		}
		fout<<"Case #"<<round<<": "<<count<<endl;
	}
}
