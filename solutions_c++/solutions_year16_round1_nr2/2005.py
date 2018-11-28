#include<bits/stdc++.h>
using namespace std;

main()
{
	freopen("round22l.in","r",stdin);
	freopen("out22l.txt","w",stdout);
	int t,i,j,k=1,n;
	cin>>t;
	while(k<=t)
	{
		cin>>n;
		int h[n][2*n-1],c[2501]={0},ans[n];
		for(i=0;i<n;i++)
		{
			for(j=0;j<(2*n-1);j++)
			{
				cin>>h[i][j];
				c[h[i][j]]++;
			}
		}
		for(i=0,j=0;i<2501;i++)
		{
		//	ans[i]=0;
			if(c[i]%2!=0)
			{
				ans[j]=i;
				j++;
			}
		}
		sort(ans,ans+n);
		cout<<"Case #"<<k<<": ";
		for(i=0;i<n;i++)
		{
		//	if(ans[i]!=0)
			cout<<ans[i]<<" ";
		}
	//	cout<<"hello";
		cout<<endl;
	//		cout<<"hello";
		k++;
	}
}
