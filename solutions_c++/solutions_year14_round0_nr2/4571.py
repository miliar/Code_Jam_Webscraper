#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int t;
	double c,f,x,s,v;
	cin>>t;
	for (int i=0;i<t;++i)
	{
		cin>>c>>f>>x;
		s=0;v=2;
		while (x/v>c/v+x/(v+f))
		{
			s+=c/v;
			v+=f;
		}
		s+=x/v;
		printf("case #%d: %.7f\n",i+1,s);
	}
}
