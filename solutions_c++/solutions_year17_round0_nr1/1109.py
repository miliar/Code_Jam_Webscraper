#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		string s;
		cin>>s;
		int k,i,j,n=s.length();
		cin>>k;
		int ans=0;
		for(i=0;i<=n-k;i++)
		{
			if(s[i]=='-')
			{
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else s[j]='+';
				}
				ans++;
			}
		}
		for(;i<n;i++)
		{
			if(s[i]=='-')
				break;
		}
		cout<<"Case #"<<z<<": ";
		if(i<n)
			cout<<"IMPOSSIBLE\n";
		else cout<<ans<<endl;
	}
	return 0;
}