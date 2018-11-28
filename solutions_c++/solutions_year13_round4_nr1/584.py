#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
long long MOD = 1000002013;
class Interval
{
public:
	long long o;
	long long e;
	Interval(long long o_ = 0,long long e_ = 0)
	{
		o=o_;
		e=e_;
	}
};
bool operator < (const Interval &a,const Interval &b)
{
	if (a.o!=b.o)
		return a.o<b.o;
	else return a.e<b.e;
}
int main()
{
	long long T,N,M,o,e,p;
	Interval a[10005];
	cin>>T;
	for (int cs=1;cs<=T;cs++)
	{
		cin>>N>>M;
		long long cnt = 0;
		for (long long i=0;i<M;i++)
		{
			cin>>o>>e>>p;
			for (long long j=0;j<p;j++)
			{
				a[cnt] = Interval(o,e);
				cnt++;
			}
		}
		long long ori=0,aft=0,cha;
		for (long long i=0;i<cnt;i++)
		{
			cha = a[i].e-a[i].o;
			ori += (N+N-(cha-1))*cha/2;
		}
		sort(a,a+cnt);
		bool flag = true;
		while(flag)
		{
			flag = false;
			for (long long i=0;i<cnt-1;i++)
			{
				for (long long j = i+1;j<cnt;j++)
				{
					if (a[i].o<a[j].o && a[i].e>=a[j].o && a[i].e<a[j].e)
					{
						cha = a[i].e;
						a[i].e = a[j].e;
						a[j].e = cha;
						flag = true;
					}
				}
			}
			sort(a,a+cnt);
		}
		for (long long i=0;i<cnt;i++)
		{
			cha = a[i].e-a[i].o;
			aft += (N+N-(cha-1))*cha/2;
		}
		cout<<"Case #"<<cs<<": "<<(ori-aft)%MOD<<endl;
	}

	return 0;
}