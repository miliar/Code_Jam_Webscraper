#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	// your code goes here
	freopen("A-large.in","r",stdin);
	freopen("output_file_name_large.txt","w",stdout);
	long long test;
	cin>>test;
	long long cas;
	for(cas=1;cas<=test;cas++)
	{
		long long n;
		cin>>n;
		long long a[n],i,sum=0,sum1=0;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		for(i=0;i<n-1;i++)
		{
			if(a[i]>a[i+1])
			{
				sum+=a[i]-a[i+1];
			}
		}
		long long elem,max_diff=0;
		for(i=0;i<n-1;i++)
		{
			if(max_diff<a[i]-a[i+1])
			{
				max_diff=a[i]-a[i+1];
			}
		}
		if(max_diff>0)
		{
			for(i=0;i<n-1;i++)
			{
				if(a[i]<=max_diff)
				{
					sum1+=a[i];
				}
				else
					sum1+=max_diff;
			}
		}

		cout<<"Case #"<<cas<<": "<<sum<<" "<<sum1<<endl;
	}
	return 0;
}
