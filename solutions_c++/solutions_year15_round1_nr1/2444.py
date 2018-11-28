#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define lli long long int
#define gc getchar

using namespace std;

void scan(lli &x)
{
    register lli c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	lli t,n,ans1,temp,sum,max,ans2;
	double rate;
	cin>>t;
	for(lli z=1;z<=t;z++)
	{
		max=0;
		ans2=0;
		sum=0;
		ans1=0;
		cin>>n;
		lli arr[n];
		for(lli i=0;i<n;i++)
		{
			cin>>arr[i];
			sum+=arr[i];
		}
		//rate=sum/((float)n * 10.0);
		for(lli i=1;i<n;i++)
		{
			if(arr[i-1]>arr[i])
			{
				ans1+=arr[i-1]-arr[i];
				temp=arr[i-1]-arr[i];
				if(max<temp)
				max=temp;
			}
		}
		//cout<<"max is"<<max<<endl;
		for(lli i=0;i<n-1;i++)
		{
			if(max>=arr[i])
			{
				ans2+=arr[i];
			}
			else
			{
				ans2+=max;
			}
		}
		cout<<"Case #"<<z<<": "<<ans1<<" "<<ans2<<endl;
	}
	
	return 0;
}
