#include<iostream>
#include<stdio.h>
using namespace std;
double rec(double c,double f,double x,double tottime,double cook)
{
	double ammma,ila;
	ammma=(c/cook)+(x/(cook+f));
	ila=(x/cook);
	if(ammma<ila)
		return rec(c,f,x,tottime+(c/cook),cook+f);
	return tottime+(x/cook);
}
int main()
{
	double c,f,x,cook=2;
	double tottime=0.0;
	int flag=0,t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>c>>f>>x;
		cook=2;
		tottime=0.0;
		tottime=rec(c,f,x,tottime,cook);
		printf("Case #%d: %0.7lf\n",i+1,tottime);
	}
	return 0;
}