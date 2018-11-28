// QualRound.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "vector"
#include "string"
#include "algorithm"
#include "string.h"
#include "stdio.h"
#include "iostream"
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		long long n;
		cin>>n;
		cout<<"Case #"<<tc+1<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		long long cur = n;
		int mask = 0;
		for(int j=0;j<1000;j++)
		{
			long long t=cur;
			while(t)
			{
				mask|=1<<(t%10);
				t/=10;
			}
			if(mask==(1<<10)-1)
				break;
			cur+=n;
		}
		if(mask==(1<<10)-1)
			cout<<cur<<endl;
		else 
			cout<<"INSOMNIA"<<endl;
	}
	return 0;
}

