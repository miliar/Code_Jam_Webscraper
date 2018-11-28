#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		int n,i,j,ds=0,s=0;
		cin>>n;
		double a[n],b[n];
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		for(i=n-1,j=n-1;i>=0,j>=0;i--,j--)
		{
			if(a[i]>b[j])
				ds++;
			else
			{
				i++;
			}
		}
		s=n;
		for(i=0,j=0;i<n,j<n;i++,j++)
		{
			if(a[i]<b[j])
			{
				s--;
			}
			else
				i--;
		}
		cout<<"Case #"<<k<<": ";
		cout<<ds<<" "<<s<<endl;
	}
}