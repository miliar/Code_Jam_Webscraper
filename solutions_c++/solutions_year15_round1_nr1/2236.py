#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
int main()
{
	if( true)
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	}
	long long ans1,ans2;
	int t;
	cin>>t;
	for(int k=1;k<=t;++k)
	{
		ans1=ans2=0;
		int n;
		cin>>n;
		vector<long long> a(n);
		for(int i=0;i<n;++i)
			cin>>a[i];
		for(int i=0;i<n-1;++i)
			if(a[i+1]<a[i])
				ans1+=a[i]-a[i+1];
		long long rate=0;
		for(int i=0;i<n-1;++i)
		{
			long long dif=a[i]-a[i+1];
			if(dif<=0)
				continue;
			rate=max(rate, dif);
		}
		for(int i=0;i<n-1;++i)
		{
			long long dif=a[i]-a[i+1];
			ans2+=min(a[i],rate);

		}
		cout<<"Case #"<<k<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}