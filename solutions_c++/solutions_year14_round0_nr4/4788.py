#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t,n,j=1,i;
	cin>>t;
	while(j<=t)
	{
		cin>>n;
		int dwar=n,war=0,start,end;
		double a[n],b[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		std::sort(a,a+n);
		for(i=0;i<n;i++)
		{
			cin>>b[i];
		}
		std::sort(b,b+n);
		start=0;end=n-1;
		for(i=n-1;i>=0;i--)
		{
			if(a[i]>b[end])
			{
				start++;war++;
			}
			else
			{
				end--;
			}
		}
		start=0;end=n-1;
		for(i=0;i<n;i++)
		{
			if(a[i]<b[start])
			{
				dwar--;
				end--;
			}
			else start++;
		}
		cout<<"Case #"<<j<<": "<<dwar<<" "<<war<<"\n";
		j++;
	}	
	return 0;
}
