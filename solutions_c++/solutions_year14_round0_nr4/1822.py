#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
		
		int n;
		cin>>n;
		double a[n],b[n];
		for (int i=0;i<n;i++)
			cin>>a[i];
		for (int i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int ans = 0;
		int la=0,lb=0,ra=n-1,rb=n-1;
		while (la<=ra)
		{
			if (a[la]<b[lb])
			{
				la++;
				rb--;
			}
			else
			{
				ans++;
				la++;
				lb++;
			}
		}
		cout<<"Case #"<<tt<<": ";
		cout<<ans<<" ";
		la = 0; lb = 0;
		while (lb<n-1)
		{
			while(a[la]>b[lb] & lb<n-1)
				lb++;
			if (lb<n-1)
			{
				la++;
				lb++;
			}
		}
		//cout<<"lalb"<<la<<lb<<endl;
		if (a[la]<b[lb]) cout<<n-la-1<<"\n";
		else cout<<n-la<<"\n";
	}
	return 0;
}