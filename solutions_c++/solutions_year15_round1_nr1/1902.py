#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,tt,n,i,a[1003],minv,ans1,ans2;
	cin>>tt;
	for(t=1;t<=tt;t++)
	{
		cin>>n>>a[0];
		minv=1000000;
		ans1=ans2=0;
		for(i=1;i<n;i++)
		{
		cin>>a[i];
		minv=min(minv,a[i]-a[i-1]);
		if(a[i]<a[i-1])
			ans1+=a[i-1]-a[i];
		}
		minv=-minv;
		for(i=0;i<n-1;i++)
			ans2+=min(minv,a[i]);
		cout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<"\n";
	}
}