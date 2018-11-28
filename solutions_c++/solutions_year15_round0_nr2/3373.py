//be name khoda

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		int n,a[1010],ans=111111111,m;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			m=max(m,a[i]);
		}
		sort(a,a+n);
		for(int i=m;i>=1;i--)
		{
			int o=i;
			for(int j=n-1;j>=0 && a[j]>i;j--)
				o+=(a[j]+i-1)/i-1;
			ans=min(ans,o);
		}
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
