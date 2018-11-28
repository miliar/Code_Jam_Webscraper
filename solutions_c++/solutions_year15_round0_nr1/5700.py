#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int s;
		string arr;
		cin>>s;
		cin>>arr;
		int ovat=0,ans=0;
		for(int i=0;i<arr.length();i++)
		{
			if(i==0)
				ovat+=arr[i]-'0';
			else
			{
				if(i>ovat)
				{
					ans+=i-ovat;
					ovat=i;
				}
				ovat+=arr[i]-'0';
			}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
