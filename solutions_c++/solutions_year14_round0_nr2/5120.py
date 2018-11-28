#include<map>
#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
double fun(double prod,double f,double c,double x)
{
	if((x/prod)<=(c/prod)+(x/(prod+f)))	return (x/prod);
	return min(x/prod,(c/prod)+fun(prod+f,f,c,x));
}
int main()
{	
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double ans=min((x/2.000000),(c/2.000000)+fun(f+2.000000,f,c,x));
		printf("Case #%d: %.7lf\n",ii,ans);
	}
	return 0;
}
