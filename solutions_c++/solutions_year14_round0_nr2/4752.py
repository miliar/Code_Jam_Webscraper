#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

double check(double c,double f,double x,double ck,double r,double t)
{
	
	//cout<<(x-ck+c)/(r+f)<<" "<<(x-ck)/r<<endl;
	if(x/(r+f)>(x-c)/r) return t+(x)/r;
	
	else return check(c,f,x,ck,r+f,t+c/r);
}

int main()
{
	double t,c,f,x;cin>>t;
	for(int i=0;i<t;i++)
	{
	cin>>c>>f>>x;
	//cout<<c<<f<<x<<endl;
	cout<<"Case #"<<i+1<<": ";printf("%.17g\n", check(c,f,x,0.00000000,2.00000000,0.000));cout<<endl;
}}
