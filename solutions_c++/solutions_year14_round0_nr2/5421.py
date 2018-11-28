#include<iostream>
#include<stdio.h>
#include<string>
#include<cstdio>
#include <sstream>

using namespace std;

void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;cin>>t;
	for(int i=1;i<=t;++i)
	{
		long double get=2;
		long double c,f,x;
		cin>>c;
		cin>>f;
		cin>>x;
		long double backtime=c/f;
		long double time=0;
		while(backtime*(get+f)<=x)
		{
			time+=c/get;
			get+=f;
		}
		time+=(x/get);
		cout<<"Case #"<<i<<": ";
		printf("%20.7f\n",time);
		

		
	}
}
				

