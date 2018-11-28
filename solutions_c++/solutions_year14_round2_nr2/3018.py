#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
	int t,a,b,k;
	cin>>t;
	for(int ind=1;ind<=t;ind++)
	{
		int count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
				if((i&j)<k)
					count++;
		printf("Case #%d: %d\n",ind,count);
	}
	return 0;
}
