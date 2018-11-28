#include<cstdio>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int tt=1;
	while(tt<=t)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double n = ((x*f)-(c*f)-(2*c))/(c*f);
		int nn = (int)n;
		//cout<<nn;
		double cost = 0.0;
		if(n>0)
		{
			cost  = cost + (x/(((nn+1)*f)+2));
			for(int i=0;i<=nn;i++)
				cost = cost + (c/((i*f)+2));
		}
		else
		{
			cost = x/2;
		}
		cout<<"Case #"<<tt<<": ";
		printf("%.7f\n",cost);
		tt++;
	}
	return 0;
}