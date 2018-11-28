#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
	int i,j,k,t,a,b,co,d;
	long long int n;
	scanf("%d",&t);
	co=0;
	while(t--)
	{
		++co;
		n=0;
		scanf("%d%d%d",&a,&b,&k);
		for(i=0;i<a;++i)
		{
			for(j=0;j<b;++j)
			{
				d=i&j;
				if(d<k) ++n;
			}
		}
		printf("Case #%d: %lld\n",co,n);
	}
	return 0;
}