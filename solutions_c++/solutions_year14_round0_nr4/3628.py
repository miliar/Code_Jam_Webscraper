#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

int main()
{
	int t;
	long long n,war,dwar;
	double niom[10001],ken[10001],a,b;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		war=dwar=0;
		printf("Case #%d:",i);
		scanf("%lld",&n);
		for(int j=0;j<n;j++)
			scanf("%lf",&niom[j]);
		for(int j=0;j<n;j++)
			scanf("%lf",&ken[j]);
		sort(niom,niom+n);
		sort(ken,ken+n);
		int tmp=0;
		for(int j=0;j<n;j++)
		{
			for(int k=tmp;k<n;k++)
			{
				if(niom[j]<ken[k])
				{
					war++;
					tmp=k+1;
					break;
				}
			}
		}
		tmp=0;
		for(int j=0;j<n;j++)
		{
			for(int k=tmp;k<n;k++)
			{
				if(niom[k]>ken[j])
				{
					dwar++;
					tmp=k+1;
					break;
				}
			}
		}	
		printf(" %lld %lld\n",dwar,n-war);
	}
	return 0;
}
