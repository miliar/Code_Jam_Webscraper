// cj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

#include<vector>
#include<algorithm>
#include<functional>

#define res(i) cout<<"Case #"<<i<<": "
#define fo(c)for(int i=0;i<c;i++)
int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	cin>>n;

	for(int a=1;a<=n;a++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double d=2;
		double ans=0;
		while(true){
			double t1=x/d;
			double t2=c/d;
			d+=f;
			double t3 = x/d;
			if (t1<t2+t3)
			{
				res(a)<<fixed<<setprecision(7)<<ans+t1<<endl;
				break;
			}
			ans+=t2;
			
		}
		
	}
	return 0;
}

