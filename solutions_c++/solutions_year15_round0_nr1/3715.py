#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int s;
		cin>>s;
		char shy[s+1];
		cin>>shy;
		long long ans=0,sh=0;
		for(int j=0;j<=s;j++)
		{
			if(j>sh)
			{
				ans+=j-sh;
				sh=j;
			}
			sh+=shy[j]-'0';
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
