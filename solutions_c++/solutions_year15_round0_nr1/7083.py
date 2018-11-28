#include<bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int t,i,shy,z;
	long long count,ans;
	string s;
	cin>>t;
	z=t;
	while(t--)
	{
		cin>>shy;
		cin>>s;
		count=s[0]-'0';
		ans=0;
		for(i=1;i<=shy;i++)
		{
			if(count<i)
			{
				ans++;
				count++;
			}
			count+=(s[i]-'0');
		}
		cout<<"Case #"<<z-t<<": "<<ans<<"\n";
	}
	return 0;
}