#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
double c;
double f;
double x;
double cookie;
double time;

int t;
int n=1;

time =0;
cin>>t;

while(t!=0)
{
	cin>>c;
	cin>>f;
	cin>>x;
	double i=0;
	cookie=0;
	double m=2;
	time=0;
	double p,q,r;
	while(cookie<x)
	{
		p=((c-cookie)/m);
		q=(x/(m+f));
		r=((x-cookie)/m);
		if(r<(p+q))
		{
			time+=r;
			break;
		}
		else
		{
			time+=p;
			cookie=0;
			m+=f;
		}
	}
	cout<<"Case #"<<n<<": ";
	cout << std::fixed;
	cout.precision(7);
	cout<<time<<endl;
	t--;
	n++;
	
}
}