#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#define MAX(a,b) a>b?a:b;
#define MIN(a,b) a<b?a:b;
typedef long long int lld;
using namespace std;

int main()
{
	int t,n,count,count2,i,j;
	int max_pt,min_pt;
	double a[1200],b[1200];
	cin>>t;
	int x=0;
	while(t--)
	{
		x++;
		cin>>n;
		for(i=0;i<n;i++)
		cin>>a[i];
		for(i=0;i<n;i++)
		cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		j=count=0;
		for(i=0;i<n;i++)
		{
			while(a[j]<b[i] && j<n)
			{
				j++;
			}
			if(j<n)
			{
				
				count++;
			//	cout<<i<<" "<<j<<" "<<count<<endl;
				j++;
			}
			
		}
		max_pt=n-1;
		min_pt=0;
		count2=0;
		for(i=n-1;i>=0;i--)
		{
			if(a[i]<b[max_pt] && max_pt>=0)
			{
				max_pt--;
			}
			else if( a[i]>b[max_pt]  && min_pt<n)
			{
				count2++;
				min_pt++;
			}
		}
		cout<<"Case #"<<x<<": "<<count<<" "<<count2<<endl;
	}
	return 0;
}
