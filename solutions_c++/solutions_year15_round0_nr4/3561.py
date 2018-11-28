#include <iostream>
using namespace std;
int fn(double x,double r,double c)
{
if(((int)(c*r))%((int)x)!=0)
{return 1;}
if(x/2.0!=1 && (x/2.0>=c || x/2.0>=r))
{return 1;}
if(x>c && x>r)
{return 1;}
return 0;
}
int main() {
	double t,x,c,r;
	int a=0;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		
		cin>>x>>r>>c;
	  a=fn(x,r,c);
if(a)
	{cout<<"Case #"<<i<<": "<<"RICHARD"<<"\n";}
else
	{cout<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";}
		
	}
	return 0;
}