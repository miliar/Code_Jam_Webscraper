#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,i,k;
	cin >>t;
	for(i=1;i<=t;i++)
	{
		int n,count,ans=0,temp;
		cin >>n;
		string a;
		cin >> a;
		count=a[0]-'0';
		for(k=1;k<=n;++k)
		{
			temp=a[k]-'0';
			if(count<k)
			{
			ans =ans+(k-count);
			count=k;
			}
			count=count+temp;
		}
	cout <<"Case #"<<i<< ": "<<ans<<endl;
	}
}
