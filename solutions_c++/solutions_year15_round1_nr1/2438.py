#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		int arr[1015];
		cin>>n;
		int val=-1;
		int ans1=0,ans2=0;
		for(int j=0;j<n;j++)
		{
			cin>>arr[j];
			if(j>0)
			{
				if(arr[j]<arr[j-1])
				{
					val=max(val,arr[j-1]-arr[j]);
					ans1+=arr[j-1]-arr[j];
				}
			}
		}
		for(int j=0;j<n-1;j++)
		{
			if(val!=-1)
				ans2+=min(arr[j],val);
		}
		cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
