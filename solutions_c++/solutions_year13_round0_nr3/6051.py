// C.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<cstdio>
#include<vector>
#define M 10000001
using namespace std;

vector<long long>v;

int IsPal(int n)
{
	int r = 0,m=n;
	while(n)
	{
		r = r*10+n%10;
		n/=10;
	}
	if (r==m)return 1;
	return 0;
}


int main()
{
	long long i,j,a,b,tmp;
	int t,p,k;

	for(i=1;i<=M;i++)
	{
		if(IsPal(i)&&IsPal(i*i))
			v.push_back(i*i);
	}

	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>a>>b;
		int cnt = 0,s = v.size();
		for(p=0;p<s;p++)
			if(v[p]>=a&&v[p]<=b)cnt++;
		printf("Case #%d: %d\n", k, cnt);
	}

	return 0;
}

