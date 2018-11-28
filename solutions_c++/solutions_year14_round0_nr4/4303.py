#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t,l;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	cin>>t;
	for(l=1;l<=t;l++)
	{
		int i,j,k=0,n,m=0;
		cin>>n;
		double a[n],b[n];
		for(i=0;i<n;i++)
		scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
		scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		i=0;j=0;
		while(i<n&&j<n)
		{
			if(a[i]<b[j])
			{
				i++;j++;m++;
			}
			else
			{
				j++;
			}
		}
		i=0;j=0;
		while(i<n&&j<n)
		{
			if(a[i]<b[j])
			{
				i++;
			}
			else
			{
				i++;j++;k++;
			}
		}
		printf("Case #%d: %d %d\n",l,k,n-m);
	}
	return 0;
}
