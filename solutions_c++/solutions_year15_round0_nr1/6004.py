#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int sm,arr[1005];
		cin>>sm;
		string s;
		cin>>s;
		for(int i=0;i<s.length();i++)
			arr[i]=s[i]-'0';
		int sum=0;
		int ans=0;
		for(int i=0;i<=sm;i++)
		{
			if(sum<i)
			{
				int temp=i-sum;
				ans+=temp;
				sum+=temp;
			}
			sum+=arr[i];
		}
		cout<<"Case #"<<j<<": "<<ans<<"\n";
	}
	return 0;
}


