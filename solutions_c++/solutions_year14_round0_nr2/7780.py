#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<algorithm>
#include<iomanip>
using namespace std;
int main()
{
	int t,p=1;
	cin>>t;
	while(t--)
	{
		long double c,f,x,time=0,factor=2.0;
		cin>>c>>f>>x;
		while(1)
		{
			if((x/factor)<(c/factor)+(x/(factor+f)))
			{
				time=time+x/factor;
				break;
			}
			time=time+c/factor;
			factor=factor+f;
		}
		cout<<fixed;
		cout<<"Case #"<<p<<":"<<" "<<setprecision(7)<<time<<"\n";
		p++;	
	}
	return 0;
}
