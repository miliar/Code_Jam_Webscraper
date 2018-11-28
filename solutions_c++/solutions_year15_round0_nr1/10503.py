#include<bits/stdc++.h>
using namespace std;
main()
{
	int T;
	int var=0;
	cin>>T;
	while(T--)
	{
		int n;
		string s;
		cin>>n>>s;
		int ans=0;
		ans=s[0]-'0';
		int ans1=0;
		for(int i=1;i<=n;i++)
		{
			int temp=s[i]-'0';
			if(ans<i)
			{
				ans1+=i-ans;
				ans+=(temp+i-ans);
			}
			else
			{
				ans+=temp;
			}
		}
		cout<<"Case #"<<var+1<<": "<<ans1<<endl;var++;	
	}
}
