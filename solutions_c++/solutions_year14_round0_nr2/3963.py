#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	double x,c,f,tm;
	short int t,count=0;
	cin>>t;
	while(t--)
	{
		count++;
		cin>>c>>f>>x;
		double r=2.0;
		tm=0.0;
		while(((c/r)+(x/(r+f)))<(x/r))
		{
			tm+=c/r;
			r+=f;
		}
		tm+=x/r;
		printf("Case #%hd: %.7lf\n",count,tm);
	}
	return 0;
}
