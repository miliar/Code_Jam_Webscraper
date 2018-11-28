#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,te=1;
	cin>>t;
	while(te!=t+1)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<te<<": ";
		te++;
		int ans=1;
		char pre=s[0],m='-';
		for(int i=0;i<s.length();i++)
		{
			if(s[i]!=pre)
			{
				ans+=1;
				pre=s[i];
			}
		}
		if(pre==m)
			cout<<ans<<endl;
		else
			cout<<ans-1<<endl;
	}
	return 0;
}