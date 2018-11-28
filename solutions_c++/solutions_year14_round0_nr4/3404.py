
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main()
{
	int t,n,i,j,l;
	cin>>t;
	int ca =0;
	while(t--)
	{
		ca++; 
		cin>>n;
		int a1=0,a2=0;
		double a[n],b[n];
		for(i=0;i<n;i++)
			cin>>a[i];
		for( i=0;i<n;i++)
			cin>>b[i];
		i=0,j=0;
		sort(a,a + n);
		sort(b,b + n);
		for(int k=0;k<n;k++)
		{
			if(j>=n)
			{
				break;
			}
			if(a[i]<b[j])
			{
				i++,j++;
			}
			else
				j++;
		}
		a1=n-i;
		i=0,j=0,l=n-1;
		for(int k=0;k<n;k++)
		{
			if(a[i]>b[j])
			{
				a2++;
				i++,j++;
			}
			else
			{
				b[l]=1.9;
				l--;
				i++;
			}
		}
		cout<<"Case #"<<ca<<": "<<a2<<" "<<a1<<endl;
	}
	return 0;
}
