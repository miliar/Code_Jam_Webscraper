#include <iostream>
#include <cmath>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <sstream>

using namespace std;

bool check(long long number)
{
	long long  Lsqroot=sqrtl(number);
	double dsqroot=sqrtl(number);
	if(Lsqroot!=dsqroot)
		return false;

	string snum;
	stringstream ss;
	ss<<number;
	ss>>snum;
	int L=snum.length();

	for(int i=0;i<L;i++)
	{
		if(snum[i]!=snum[L-i-1])
			return false;
	}
	stringstream sss;
	string temp;
	sss<<Lsqroot;
	sss>>temp;

	L=temp.length();

	for(int i=0;i<L;i++)
	{
		if(temp[i]!=temp[L-i-1])
			return false;
	}

	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int testcases;
	cin>>testcases;
	for(int i=1;i<=testcases;i++)
	{
		long long x,y;
		cin>>x>>y;
		long long result=0;
		for(long long j=x;j<=y;j++)
		{
			if(check(j))
				result++;
		}
		cout<<"Case #"<<i<<": "<<result<<endl;
	}

	return 0;
}