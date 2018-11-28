#include <bits/stdc++.h>
using namespace std;
double func(double c, double a, double f, double x)
{
	double foo;
		foo=0;
		int n=1000000;
		for(int i=n;i>=0;i--)
		{
			foo=min(x/(a+i*f),c/(a+i*f)+foo);
		}
		return foo;
}
int main() {
	int t,n,i;double c,f,x;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		cout<<"Case #"<<i<<": ";
		printf("%.10f\n",func(c,2,f,x));

	}
	// your code goes here
	return 0;
}
