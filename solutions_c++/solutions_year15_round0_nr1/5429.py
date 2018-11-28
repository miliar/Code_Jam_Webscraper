	#include <bits/stdc++.h>
	using namespace std;
	int main()
	{
		freopen("in.txt", "r", stdin);
		freopen("out3.txt", "w", stdout);
		
		int t;
		cin>>t;
		for(int test=1;test<=t;test++)
		{
			int curr=0,ans=0,n;
			string arr;
			cin>>n;
			cin>>arr;
			curr=arr[0]-48;
			for(int i=1;i<=n;i++)
			{
				if(i>curr&&arr[i]-48>0)
				{
					ans+=(i-curr);
					curr+=(i-curr);
				}
				curr+=(arr[i]-48);
				// cout<<curr<<" ";
			}
			cout<<"Case #"<<test<<": ";
			cout<<ans<<"\n";
		}
		return 0;
	}
