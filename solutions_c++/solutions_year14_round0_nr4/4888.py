#include <iostream>
#include <cstdio>
#include <algorithm>
#include <deque>
using namespace std;

double a[1005],b[1005];

deque<double> a1;
deque<double> b1;

int main() 
{
	int t,i,j,k,n,co,nw,ndw;
	scanf("%d",&t);
	co=0;
	while(t--)
	{
		++co;
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%lf",&a[i]);
		for(i=0;i<n;++i)
			scanf("%lf",&b[i]);
		
		sort(a,a+n); sort(b,b+n);
		
		for(i=0;i<n;++i) 
		{
			a1.push_back(a[i]);
			b1.push_back(b[i]);
		}
		
		i=j=k=0;
		while(i<n && j<n)
		{
			if(a[i]<b[j])
			{
				++i; ++j; ++k;
			}
			else
			{
				++j;
			}
		}
		nw=n-k;
		
		ndw=0;
		while(!a1.empty())
		{
			if(a1.front()<b1.front())
			{
				a1.pop_front();
				b1.pop_back();
			}
			else
			{
				a1.pop_front();
				b1.pop_front();
				++ndw;
			}
		}
		
		/*ndw=0;
		for(i=0;i<n;++i)
		{
			if(a[i]>b[i]) ++ndw;
		}
		for(i=0;i<n/2;++i)
		{
			k=b[i];
			b[i]=b[n-i-1];
			b[n-i-1]=k;
		}
		k=0;
		for(i=0;i<n;++i)
		{
			if(a[i]>b[i]) ++k;
		}
		if(k>ndw) ndw=k;
		*/
		
		printf("Case #%d: %d %d\n",co,ndw,nw);
		
		
	}
	return 0;
}