#include <cstdio>
#include <iostream>
using namespace std;

int t;
int main()
{
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		double C,F,X,factor=2.0,ans=0.0,it;
		cin>>C>>F>>X;
		it = ( X/(factor+F) )+(C/factor);
		while(it < (X/factor))
		{
			ans += (C/factor);
			factor += F;
			it = ( X/(factor+F) )+(C/factor);
		}
		ans += X/factor;
		printf("Case #%d: %.7f\n",i+1,ans );
	}
	return 0;
}